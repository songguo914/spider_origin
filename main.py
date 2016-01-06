#-*- coding:utf-8 -*-
'''
Author: liujingmin
'''
from common.const import PROJECT
from spider.config_process import ConfigProcess

if __name__ == "__main__":
    conf_process = ConfigProcess()
    conf_process.load()
    print PROJECT.SavePath
    print PROJECT.UrlPath
