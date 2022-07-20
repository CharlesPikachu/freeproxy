'''
Function:
    setup the freeproxy
Author:
    Charles
微信公众号:
    Charles的皮卡丘
GitHub:
    https://github.com/CharlesPikachu
'''
import freeproxy
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


'''setup'''
setup(
    name=freeproxy.__title__,
    version=freeproxy.__version__,
    description=freeproxy.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    author=freeproxy.__author__,
    url=freeproxy.__url__,
    author_email=freeproxy.__email__,
    license=freeproxy.__license__,
    include_package_data=True,
    install_requires=[lab.strip('\n') for lab in list(open('requirements.txt', 'r').readlines())],
    zip_safe=True,
    packages=find_packages()
)