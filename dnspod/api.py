#!/usr/bin/env python
#-*- coding: utf-8 -*-

from base import BaseAPI
from info import InfoAPI
from domain import DomainAPI
from record import RecordAPI

class DNSPodAPI(object):
    '''
    User API object
    '''

    def __init__(self, login_email, login_password, **kwargs):
        self._base_api = BaseAPI(login_email, login_password, **kwargs)
        self.info = InfoAPI(self._base_api)
        self.domain = DomainAPI(self._base_api)
        self.record = RecordAPI(self._base_api)
