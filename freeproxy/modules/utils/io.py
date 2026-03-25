'''
Function:
    Implementation of IO Related Operations
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import os
import time
from pathlib import Path
fcntl = __import__("fcntl") if os.name != "nt" else None
msvcrt = __import__("msvcrt") if os.name == "nt" else None


'''touchdir'''
def touchdir(directory, exist_ok=True, mode=511):
    return os.makedirs(directory, exist_ok=exist_ok, mode=mode)


'''FileLock'''
class FileLock:
    def __init__(self, lock_path: Path, timeout: float = 300.0, poll_interval: float = 0.2):
        self.fp = None
        self.timeout = timeout
        self.lock_path = Path(lock_path)
        self.poll_interval = poll_interval
    '''enter'''
    def __enter__(self):
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        self.fp = open(self.lock_path, "a+b"); self.fp.seek(0, os.SEEK_END)
        if self.fp.tell() == 0: self.fp.write(b"\0"); self.fp.flush()
        deadline = time.time() + self.timeout
        while True:
            try:
                if os.name == "nt": self.fp.seek(0); msvcrt.locking(self.fp.fileno(), msvcrt.LK_NBLCK, 1)
                else: fcntl.flock(self.fp.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                return self
            except OSError:
                if time.time() >= deadline: raise TimeoutError(f"Timeout acquiring lock: {self.lock_path}")
                time.sleep(self.poll_interval)
    '''exit'''
    def __exit__(self, exc_type, exc, tb):
        try:
            if not self.fp: return
            if os.name == "nt": self.fp.seek(0); msvcrt.locking(self.fp.fileno(), msvcrt.LK_UNLCK, 1)
            else: fcntl.flock(self.fp.fileno(), fcntl.LOCK_UN)
        finally:
            if self.fp: self.fp.close(); self.fp = None