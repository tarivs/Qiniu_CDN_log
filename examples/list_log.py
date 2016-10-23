#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '..'))

from qiniu import Auth, BucketManager

if __name__ == "__main__":
    access_key = "..."
    secret_key = "..."
    # 初始化Auth状态
    q = Auth(access_key=access_key, secret_key=secret_key)
    buck = BucketManager(q)

    # 日期
    day = "2016-10-13"

    # 域名列表，以英文分号 ; 分割
    domains = "a.qiniu.com;b.qiniu.com"

    ret, eof, info = buck.list_log(day, domains)

    print 'ret :', ret
    print 'info :', info
