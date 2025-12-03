# FreeProxy Installation

#### Environment Requirements

- Operating system: Linux, macOS, or Windows.
- Python version: Python 3.9+ with requirements in [pyfreeproxy requirements.txt](https://github.com/CharlesPikachu/freeproxy/blob/master/requirements.txt).

#### Installation Instructions

You have three installation methods to choose from,

```sh
# from pip
pip install pyfreeproxy
# from github repo method-1
pip install git+https://github.com/CharlesPikachu/freeproxy.git@master
# from github repo method-2
git clone https://github.com/CharlesPikachu/freeproxy.git
cd freeproxy
python setup.py install
```

Please note that some proxy sources need to be crawled using [Playwright](https://playwright.dev/). 
Playwright will automatically download and configure the browser drivers, so there is no need to worry — it is not malware. 
For more details, you can refer to the [official Playwright documentation](https://playwright.dev/docs/intro).