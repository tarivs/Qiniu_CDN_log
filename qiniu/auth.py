#!/usr/bin/python
# -*- coding: utf-8 -*-
import hmac
from hashlib import sha1
from base64 import urlsafe_b64encode
from urlparse import urlparse


class Auth(object):
    def __init__(self, access_key, secret_key):
        """初始化Auth类"""
        self.__checkKey(access_key, secret_key)
        self.__access_key = access_key
        self.__secret_key = bytes(secret_key)

    def get_access_key(self):
        return self.__access_key

    def __token(self, data):
        data = bytes(data)
        sign = hmac.new(key=self.__secret_key, msg=data, digestmod=sha1).digest()
        return bytes(urlsafe_b64encode(bytes(sign)))

    def token_of_request(self, url, body=None, content_type=None):
        """带请求体的签名（本质上是管理凭证的签名）

        Args:
            url:          待签名请求的url
            body:         待签名请求的body
            content_type: 待签名请求的body的Content-Type

        Returns:
            管理凭证
        """
        parsed_url = urlparse(url)
        query = parsed_url.query
        path = parsed_url.path
        data = path
        if query != '':
            data = ''.join([data, '?', query])
        data = ''.join([data, "\n"])

        if body:
            mimes = [
                'application/x-www-form-urlencoded'
            ]
            if content_type in mimes:
                data += body
        return '{0}:{1}'.format(self.__access_key, self.__token(data))

    @staticmethod
    def __checkKey(access_key, secret_key):
        if not (access_key and secret_key):
            raise ValueError('invalid key')
