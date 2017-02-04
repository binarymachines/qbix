#!/usr/bin/env python

#
# Generated Flask routing module for SNAP microservice framework
#



from flask import Flask, request, Response
from snap import snap
from snap import core
import json
import argparse
import sys

sys.path.append('/Users/dtaylor/workshop/binary/qbix')
import qbix_transforms

f_runtime = Flask(__name__)

if __name__ == '__main__':
    print 'starting SNAP microservice in standalone (debug) mode...'
    f_runtime.config['startup_mode'] = 'standalone'
    
else:
    print 'starting SNAP microservice in wsgi mode...'
    f_runtime.config['startup_mode'] = 'server'

app = snap.setup(f_runtime)
logger = app.logger
xformer = core.Transformer(app.config.get('services'))


#-- snap exception handlers ---

xformer.register_error_code(snap.NullTransformInputDataException, snap.HTTP_BAD_REQUEST)
xformer.register_error_code(snap.MissingInputFieldException, snap.HTTP_BAD_REQUEST)
xformer.register_error_code(snap.TransformNotImplementedException, snap.HTTP_NOT_IMPLEMENTED)

#------------------------------



#-- snap data shapes ----------


default_shape = core.InputShape("default_shape")
default_shape.add_field('id', True)

create_sample_shape = core.InputShape("create_sample_shape")
create_sample_shape.add_field('id', True)
create_sample_shape.add_field('name', False)

default_shape = core.InputShape("default_shape")
default_shape.add_field('id', True)

default_shape = core.InputShape("default_shape")
default_shape.add_field('id', True)


#------------------------------


#-- snap transform loading ----
xformer.register_transform('default', default_shape, qbix_transforms.default_func, 'application/json')
xformer.register_transform('create_sample', create_sample_shape, qbix_transforms.create_sample_func, 'application/json')
xformer.register_transform('lookup_sample', default_shape, qbix_transforms.lookup_sample_func, 'application/json')
xformer.register_transform('delete_sample', default_shape, qbix_transforms.delete_sample_func, 'application/json')

#------------------------------



@app.route('/', methods=['GET'])
def default():
    try:        
        input_data = {}
        input_data.update(request.args)
        
        transform_status = xformer.transform('default', core.convert_multidict(input_data))        
        output_mimetype = xformer.target_mimetype_for_transform('default')

        if transform_status.ok:
            return Response(transform_status.output_data, status=snap.HTTP_OK, mimetype=output_mimetype)
        return Response(json.dumps(transform_status.user_data), 
                        status=transform_status.get_error_code() or snap.HTTP_DEFAULT_ERRORCODE, 
                        mimetype=output_mimetype) 
    except Exception, err:
        logger.error("Exception thrown: ", exc_info=1)        
        raise err


@app.route('/sample', methods=['POST'])
def create_sample():
    try:
        input_data = {}
        input_data.update(request.values)
        if request.headers['Content-Type'] == 'application/json':
            input_data.update(request.get_json())
        transform_status = xformer.transform('create_sample', core.convert_multidict(input_data))        
        output_mimetype = xformer.target_mimetype_for_transform('create_sample')

        if transform_status.ok:
            return Response(transform_status.output_data, status=snap.HTTP_OK, mimetype=output_mimetype)
        return Response(json.dumps(transform_status.user_data), 
                        status=transform_status.get_error_code() or snap.HTTP_DEFAULT_ERRORCODE, 
                        mimetype=output_mimetype) 
    except Exception, err:
        logger.error("Exception thrown: ", exc_info=1)        
        raise err


@app.route('/sample/<id>', methods=['GET'])
def lookup_sample(id):
    try:        
        input_data = {}
        input_data.update(request.args)        
        input_data['id'] = id
        
        transform_status = xformer.transform('lookup_sample', core.convert_multidict(input_data))        
        output_mimetype = xformer.target_mimetype_for_transform('lookup_sample')

        if transform_status.ok:
            return Response(transform_status.output_data, status=snap.HTTP_OK, mimetype=output_mimetype)
        return Response(json.dumps(transform_status.user_data), 
                        status=transform_status.get_error_code() or snap.HTTP_DEFAULT_ERRORCODE, 
                        mimetype=output_mimetype) 
    except Exception, err:
        logger.error("Exception thrown: ", exc_info=1)        
        raise err


@app.route('/sample/<id>', methods=['DELETE'])
def delete_sample(id):
    try:        
        input_data = {}
        input_data.update(request.args)        
        input_data['id'] = id
        
        transform_status = xformer.transform('delete_sample', core.convert_multidict(input_data))        
        output_mimetype = xformer.target_mimetype_for_transform('delete_sample')

        if transform_status.ok:
            return Response(transform_status.output_data, status=snap.HTTP_OK, mimetype=output_mimetype)
        return Response(json.dumps(transform_status.user_data), 
                        status=transform_status.get_error_code() or snap.HTTP_DEFAULT_ERRORCODE, 
                        mimetype=output_mimetype) 
    except Exception, err:
        logger.error("Exception thrown: ", exc_info=1)        
        raise err





if __name__ == '__main__':
    '''If we are loading from command line,
    run the Flask app explicitly
    '''
    
    app.run(port=5000)


