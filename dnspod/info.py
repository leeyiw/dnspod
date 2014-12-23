#!/usr/bin/env python
#-*- coding: utf-8 -*-

class InfoAPI(object):
    '''
    DNSPod API start with 'Info.*'.
    '''

    def __init__(self, api):
        self._api = api

    def version(self):
        r = self._api.do_post('Info.Version')
        return r['status']['message']
