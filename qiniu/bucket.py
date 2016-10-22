#!/usr/bin/python
# -*- coding: utf-8 -*-
import http
import config
import json


class BucketManager(object):
    def __init__(self, auth):
        self.auth = auth

    def list_log(self, day, domains, token=None):
        """查询域名日志列表，获取日志的下载外链

        具体规格参考:
        http://developer.qiniu.com/article/fusion/api/log.html

        Args:
            day:        日期
            domains:    域名列表

        Returns:
            一个dict变量，类似 {"hash": "<Hash string>", "key": "<Key string>"}
            一个ResponseInfo对象
            一个EOF信息。
        """
        data = json.dumps({"day": day, "domains": domains})
        url = '{0}/v2/tune/log/list'.format(config.get_default('default_fusion_host'))
        if token is None:
            token = self.auth.token_of_request(url)
        ret, info = self.__post(url, data, token)

        eof = False
        if ret and not ret.get('marker'):
            eof = True

        return ret, eof, info

    def __post(self, url, data=None, token=None):
        return http._post_with_token(url, data, token)
