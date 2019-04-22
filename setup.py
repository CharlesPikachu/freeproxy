'''
Function:
	setup
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2019-04-08
'''
import FreeProxy
from setuptools import setup, find_packages


setup(
	name='FreeProxy',
	version=FreeProxy.__version__,
	description='ProxyTool--Collecting free proxies from internet.',
	classifiers=[
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python',
			'Intended Audience :: Developers',
			'Operating System :: OS Independent'],
	author='Charles',
	url='https://github.com/CharlesPikachu/FreeProxy',
	author_email='charlesjzc@qq.com',
	license='MIT',
	include_package_data=True,
	install_requires=['requests'],
	zip_safe=True,
	packages=find_packages()
)