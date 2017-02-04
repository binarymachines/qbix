#!/usr/bin/env python


import snap
import core
import json
import datetime



def default_func(input_data, service_objects):
    data =  {
               "name":"Invoice",
               "id":"100",
               "operation":"Create",
               "lastUpdated": datetime.datetime.now().isoformat()
           }
    return core.TransformStatus(json.dumps(data))

def create_sample_func(input_data, service_objects):
    data =  {
               "name":"Something created",
               "id":"101",
               "operation":"Create",
               "lastUpdated": datetime.datetime.now().isoformat()
           }
    return core.TransformStatus(json.dumps(data))

def lookup_sample_func(input_data, service_objects):
    raise snap.TransformNotImplementedException('lookup_sample_func')

def delete_sample_func(input_data, service_objects):
    raise snap.TransformNotImplementedException('delete_sample_func')


