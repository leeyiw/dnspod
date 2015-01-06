#!/usr/bin/env python
#-*- coding: utf-8 -*-

class DNSPodError(Exception):
    '''DNSPod error exception class'''

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message
