# 安装FreeProxy


## 环境配置

- 操作系统: Linux or macOS or Windows
- Python版本: Python3.6+


## PIP安装(推荐)

在终端运行如下命令即可(请保证python在环境变量中):
```sh
pip install pyfreeproxy --upgrade
```


## 源代码安装

#### 在线安装

运行如下命令即可在线安装:
```sh
pip install git+https://github.com/CharlesPikachu/freeproxy.git@master
```

#### 离线安装

利用如下命令下载freeproxy源代码到本地:
```sh
git clone https://github.com/CharlesPikachu/freeproxy.git
```
接着, 切到freeproxy目录下:
```sh
cd freeproxy
```
最后运行如下命令进行安装:
```sh
python setup.py install
```