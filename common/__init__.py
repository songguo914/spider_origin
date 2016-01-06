#-*- coding:utf-8 -*-
'''
Author: 刘敬民
'''
import functools


def print_log(mess):
    print mess

def func_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        flag = func(*args, **kw)
        if not flag:
            print_log("execute function: %s error!"%func.__name__)
        return flag
    return wrapper

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance
