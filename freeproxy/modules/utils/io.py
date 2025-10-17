'''
Function:
    Implementation of IO related operations
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import os


'''touchdir'''
def touchdir(directory, exist_ok=True, mode=511):
    return os.makedirs(directory, exist_ok=exist_ok, mode=mode)