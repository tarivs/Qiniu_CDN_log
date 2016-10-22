#!/usr/bin/python
# -*- coding: utf-8 -*
CDN_HOST = "http://fusion.qiniuapi.com"  # CDN管理

_config = {
    'default_fusion_host': CDN_HOST,
    'connection_timeout': 30,  # 链接超时为时间为30s
    'connection_retries': 3,  # 链接重试次数为3次
    'connection_pool': 10,  # 链接池个数为10
}


def get_default(key):
    return _config[key]
