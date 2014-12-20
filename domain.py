#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Domain(object):
    '''
    DNSPod domain
    '''

    def __init__(self, dictionary):
        for k, v in dictionary.iteritems():
            setattr(self, k, v)

class DomainAPI(object):
    '''
    DNSPod API start with 'Info.*'.
    '''

    def __init__(self, api):
        self._api = api

    def info(self, **kwargs):
        if kwargs.has_key('domain_id'):
            r = self._api.do_post('Domain.Info', domain_id=kwargs['domain_id'])
        elif kwargs.has_key('domain'):
            r = self._api.do_post('Domain.Info', domain=kwargs['domain'])
        else:
            # TODO throw exception
            pass
        return Domain(r['domain'])
