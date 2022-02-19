'''
Function:
    utils related with io operation
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import os


'''touch dir'''
def touchdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        return False
    return True