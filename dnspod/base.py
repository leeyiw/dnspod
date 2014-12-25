#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests

from info import InfoAPI

class BaseAPI(object):
    '''
    BaseAPI is used by every other API objects.

    BaseAPI hold informations that will used by other API objects during every
    API operation.
    '''

    LANG_EN = 'en'
    LANG_CN = 'cn'
    DEFAULT_LANG = LANG_EN
    DEFAULT_API_URL = 'https://dnsapi.cn/'

    def __init__(self, login_email, login_password, **kwargs):
        '''
        Initialize object with DNSPod account and options

        :Parameters:
        '''
        self.login_email = login_email
        self.login_password = login_password
        self.format = 'json'
        self.lang = kwargs.get('lang', self.DEFAULT_LANG)
        self.api_url = kwargs.get('api_url', self.DEFAULT_API_URL)

    def do_post(self, interface, **params):
        common_param = {
            'login_email': self.login_email,
            'login_password': self.login_password,
            'format': self.format,
            'lang': self.lang,
        }
        params.update(common_param)
        r = requests.post(self.api_url + interface, data=params)
        data = r.json()
        if data['status']['code'] != '1':
            # TODO throw exception
            pass
        return data
