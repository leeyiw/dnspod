#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Record(object):
    '''DNSPod record class.

    A record has a property called **line**. Line is the ISP of the request's
    source IP. User can set multiple records with same sub-domain and different
    line, then DNSPod could generate different responses for requests which has
    the same sub-domain and different line of source IP.

    :ivar str id: ID of a record
    :ivar str sub_domain: The sub-domain of the record's domain (e.g., **www** of **www.google.com**)
    :ivar str record_type: DNS record type, such as TYPE_A, etc.
    :ivar str record_line: Line of a record, such as LINE_DEFAULT, etc.
    :ivar str value: Value of a record, an IP address (e.g., '8.8.8.8')
    '''

    #: DNS record type *A*
    TYPE_A = 'A'
    #: DNS record type *NS*
    TYPE_NS = 'NS'

    #: Default line, DNSPod will use record with default line if user haven't
    #: set any record which's line match with the request line
    LINE_DEFAULT = '默认'

    def __init__(self, dictionary):
        for k, v in dictionary.iteritems():
            # transform key name from Record.List to Record.Info
            key_transform = {
                'name': 'sub_domain',
                'line': 'record_line',
                'type': 'record_type',
            }
            if k in key_transform:
                k = key_transform[k]
            setattr(self, k, v)

class RecordAPI(object):
    '''DNSPod API start with **Record.\***'''

    def __init__(self, api):
        '''Initalize object with BaseAPI

        :param api: Instance of `BaseAPI`
        '''
        self._api = api

    def list(self, domain_id, sub_domain=None):
        '''Get a list of records, for a specific domain

        :param str domain_id: Domain ID
        :param str sub_domain: Optional. Subdomain of domain
        :return: list of records
        '''
        optional_args = {}
        if sub_domain != None:
            optional_args['sub_domain'] = sub_domain
        r = self._api.do_post('Record.List', domain_id=domain_id,
                              **optional_args)
        record_list = []
        for record in r['records']:
            record['domain_id'] = domain_id
            record_list.append(Record(record))
        return record_list

    def ddns(self, domain_id, record_id, sub_domain, record_line, value):
        '''Update record's value dynamically

        If the ``value`` is different from the record's current value, then
        perform a dynamic record update. Otherwise, nothing will be done.

        :param str domain_id: Domain ID
        :param str record_id: Record ID
        :param str sub_domain: Sub domain of domain (e.g., **www** of **www.google.com**)
        :param str record_line: Line of the record
        :param str value: The record's value, an IP address
        '''
        record = self.info(domain_id, record_id)
        # If everything stay the same, no need to update
        if record.sub_domain == sub_domain and \
           record.record_line == record_line and \
           record.value == value:
            return
        self._api.do_post('Record.Ddns', domain_id=domain_id,
                          record_id=record_id, sub_domain=sub_domain,
                          record_line=record_line, value=value)

    def info(self, domain_id, record_id):
        '''Get information for a specific record

        :param str domain_id: Domain ID
        :param str record_id: Record ID
        :return: object
        '''
        r = self._api.do_post('Record.Info', domain_id=domain_id,
                              record_id=record_id)
        return Record(r['record'])
