#!/usr/bin/env python

from snap import couchbasedbx as cbx



class CouchbaseServiceObject():
    def __init__(self, logger, **kwargs):        
        self.logger = logger
        self.host = kwargs['host']
        self.data_bucket_name = kwargs['data_bucket_name']
        self.journal_bucket_name = kwargs['journal_bucket_name']
        self.cache_bucket_name = kwargs['cache_bucket_name']
        
        self.couchbase_server = cbx.CouchbaseServer(self.host)
        self.data_manager = cbx.CouchbasePersistenceManager(self.couchbase_server, self.data_bucket_name)
        self.journal_manager = cbx.CouchbasePersistenceManager(self.couchbase_server, self.journal_bucket_name)
        self.cache_manager = cbx.CouchbasePersistenceManager(self.couchbase_server, self.cache_bucket_name)


    def insert_record(self, record_type_name, record_dict):
        cb_record = cbx.CouchbaseRecordBuilder(record_type_name).add_fields(record_dict).build()
        return self.data_manager.insert_record(cb_record)

