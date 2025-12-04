# -*- coding: utf-8 -*-
"""FreeProxy client implementation.

This module provides :class:`ProxiedSessionClient` which aggregates multiple
proxy source modules, offers ``get``/``post`` helpers that automatically pick a
working proxy, and can cache the collected proxy list in Redis.
"""

import os
import json
import copy
import random
import warnings
from typing import Dict, List

# Import internal modules – the conditional import allows the file to be used as a
# script as well as a library.
if __name__ == "__main__":
    from modules import (
        BuildProxiedSession,
        ProxiedSessionBuilder,
        LoggerHandle,
        BaseProxiedSession,
        ProxyInfo,
        touchdir,
    )
else:
    from .modules import (
        BuildProxiedSession,
        ProxiedSessionBuilder,
        LoggerHandle,
        BaseProxiedSession,
        ProxyInfo,
        touchdir,
    )

warnings.filterwarnings("ignore")


class ProxiedSessionClient:
    """High‑level client that manages multiple proxied sessions.

    Parameters
    ----------
    proxy_sources: list | None
        List of source identifiers (e.g. ``['KuaidailiProxiedSession']``). If
        ``None`` all registered modules are used.
    init_proxied_session_cfg: dict | None
        Configuration passed to each source module. ``max_pages`` controls how many
        pages each crawler will fetch.
    disable_print: bool
        Forwarded to the internal logger to silence console output.
    max_tries: int
        Number of attempts before giving up on a request.
    """

    def __init__(
        self,
        proxy_sources: list = None,
        init_proxied_session_cfg: dict = None,
        disable_print: bool = False,
        max_tries: int = 5,
    ):
        # Logger
        self.logger_handle = LoggerHandle()
        # Container for the concrete session objects
        self.proxied_sessions: Dict[str, BaseProxiedSession] = {}

        # Resolve default source list
        if not proxy_sources:
            proxy_sources = list(ProxiedSessionBuilder.REGISTERED_MODULES.keys())

        # Default configuration for each source
        if init_proxied_session_cfg is None:
            init_proxied_session_cfg = {
                "max_pages": 1,
                "logger_handle": self.logger_handle,
                "disable_print": disable_print,
                "filter_rule": None,
            }

        # Initialise each source module
        for source in proxy_sources:
            try:
                cfg = copy.deepcopy(init_proxied_session_cfg)
                cfg["type"] = source
                session = BuildProxiedSession(module_cfg=cfg)
                # Trigger a crawl – ``refreshproxies`` returns a list of ProxyInfo
                candidates = session.refreshproxies()
                if not candidates:
                    # No proxies – discard the session
                    continue
                self.proxied_sessions[source] = session
            except Exception as err:
                self.logger_handle.error(
                    f"{self.__class__.__name__}.__init__ >>> {source} (Error: {err})",
                    disable_print=disable_print,
                )
                continue

        # Store runtime attributes
        self.max_tries = max_tries
        self.disable_print = disable_print
        self.proxy_sources = proxy_sources
        self.init_proxied_session_cfg = init_proxied_session_cfg

    # ---------------------------------------------------------------------
    # Helper methods
    # ---------------------------------------------------------------------
    def _choose_session(self) -> BaseProxiedSession:
        """Return a random proxied session instance.

        Raises
        ------
        RuntimeError
            If no sessions are available.
        """
        if not self.proxied_sessions:
            raise RuntimeError("No proxied sessions available")
        return random.choice(list(self.proxied_sessions.values()))

    def getrandomproxiedsession(self):
        """Return ``(name, session)`` tuple for a random session.
        """
        name = random.choice(list(self.proxied_sessions.keys()))
        return name, self.proxied_sessions[name]

    def getrandomproxy(self, proxy_format: str = "requests"):
        """Return a proxy dictionary in the requested *proxy_format*.
        """
        for _ in range(self.max_tries):
            try:
                session = self._choose_session()
                return session.getrandomproxy(proxy_format=proxy_format)
            except Exception:
                continue
        raise RuntimeError("Unable to obtain a random proxy after multiple attempts")

    # ---------------------------------------------------------------------
    # Public request methods
    # ---------------------------------------------------------------------
    def get(self, url, **kwargs):
        """Perform an HTTP GET using a random proxy.
        """
        for _ in range(self.max_tries):
            name, session = self.getrandomproxiedsession()
            session.setrandomproxy()
            try:
                self.logger_handle.info(
                    f"{self.__class__.__name__}.get >>> {url} via {session.proxies}",
                    disable_print=self.disable_print,
                )
                resp = session.get(url, **kwargs)
                resp.raise_for_status()
                return resp
            except Exception as exc:
                self.logger_handle.warning(
                    f"{self.__class__.__name__}.get >>> {url} (Error: {exc})",
                    disable_print=self.disable_print,
                )
                continue
        raise RuntimeError(f"GET request failed after {self.max_tries} attempts: {url}")

    def post(self, url, **kwargs):
        """Perform an HTTP POST using a random proxy.
        """
        for _ in range(self.max_tries):
            name, session = self.getrandomproxiedsession()
            session.setrandomproxy()
            try:
                self.logger_handle.info(
                    f"{self.__class__.__name__}.post >>> {url} via {session.proxies}",
                    disable_print=self.disable_print,
                )
                resp = session.post(url, **kwargs)
                resp.raise_for_status()
                return resp
            except Exception as exc:
                self.logger_handle.warning(
                    f"{self.__class__.__name__}.post >>> {url} (Error: {exc})",
                    disable_print=self.disable_print,
                )
                continue
        raise RuntimeError(f"POST request failed after {self.max_tries} attempts: {url}")

    # ---------------------------------------------------------------------
    # File caching
    # ---------------------------------------------------------------------
    def save_to_file(self, filepath: str = "proxies.json"):
        """Save the collected proxy list to a JSON file.
        """
        # Build the same structure that ``savetojson`` used previously
        data: Dict[str, List[dict]] = {}
        for name, session in self.proxied_sessions.items():
            data[name] = [p.todict() for p in session.candidate_proxies]
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            self.logger_handle.info(
                f"Proxies saved to file '{filepath}'", disable_print=self.disable_print
            )
        except Exception as e:
            self.logger_handle.error(
                f"Failed to write proxies to file: {e}", disable_print=self.disable_print
            )

    def load_from_file(self, filepath: str = "proxies.json") -> Dict[str, List[dict]]:
        """Load cached proxies from a JSON file.

        Returns an empty dict if the file does not exist or on error.
        """
        if not os.path.exists(filepath):
            return {}
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

# ---------------------------------------------------------------------
# Demo / simple API when executed as a script
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Example: fetch a page using a random proxy and cache the result in Redis
    demo_sources = ["KuaidailiProxiedSession"]
    demo_cfg = {"filter_rule": {"country_code": ["CN", "US"]}}
    client = ProxiedSessionClient(proxy_sources=demo_sources, init_proxied_session_cfg=demo_cfg)
    demo_headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/98.0.4758.102 Safari/537.36"
        )
    }
    try:
        response = client.get("https://space.bilibili.com/406756145", headers=demo_headers)
        print(response.text[:200])  # Print first 200 characters
    except Exception as e:
        print(f"Demo request failed: {e}")
    # Cache proxies
    client.save_to_file()