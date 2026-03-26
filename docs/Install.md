# FreeProxy Installation

#### Environment Requirements

- Operating system: Linux, macOS, or Windows.
- Python version: Python 3.10+ with requirements in [pyfreeproxy requirements.txt](https://github.com/CharlesPikachu/freeproxy/blob/master/requirements.txt).

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

Please note that some proxy sources need to be crawled using [DrissionPage](https://www.drissionpage.cn/). 
If DrissionPage cannot find a suitable browser in the current environment, it will automatically download the latest compatible beta version of Google Chrome for the current system. 
So if you notice that the program is downloading a browser, there is no need to be overly concerned.