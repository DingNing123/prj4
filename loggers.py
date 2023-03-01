'''
Python logger
1.std handler
2.file handler
CRITICAL 50 

ERROR 40 

WARNING 30 

INFO 20 

DEBUG 10 

NOTSET 0

'''
import logging
import os
import sys
import numpy as np
from transformers import BertTokenizer

def get_stderr_file_logger(log_file):
    '''
    得到root logger 
    # 这里不应该使用__name__ 否则这将不是root logger 其他的  logger信息将无法显示  
    # logger = logging.getLogger(__name__)
    '''
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    sh = logging.StreamHandler(sys.stdout)
    # sh = logging.StreamHandler(sys.stderr)
    sh.setLevel(logging.ERROR)
    format_str_sh = logging.Formatter('%(name)s[line:%(lineno)d] - %(message)s')#设置日志格式
    sh.setFormatter(format_str_sh) #设置屏幕上显示的格式
    

    fh = logging.FileHandler(log_file,'w',encoding='utf-8')
    fh.setLevel(logging.WARNING)
    format_str_fh = logging.Formatter('%(name)s[line:%(lineno)d] - %(message)s')#设置日志格式
    fh.setFormatter(format_str_fh) #设置屏幕上显示的格式
    
    if logger.hasHandlers():
        pass
    else:
        logger.addHandler(sh)
        logger.addHandler(fh)
    return logger
