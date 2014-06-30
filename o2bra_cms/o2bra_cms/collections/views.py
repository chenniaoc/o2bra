from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
import base64
from json import dumps as json_encode
import hashlib

import time

def _get_upaiPolicy_Signature():
    
    upai_policy = {}
    upai_policy['bucket'] = 'o2bratest';
    upai_policy['expiration'] = int(time.time())+60 * 5;# expired after 5 minutes
    upai_policy['save-key'] = '/{year}/{mon}/{day}/{random32}.jpg'
    #upai_policy['image-height-range'] = '0,1024'
    upai_policy = json_encode(upai_policy)
    upai_policy = base64.b64encode(upai_policy)
    signature = hashlib.md5(upai_policy+'&'+'yRjQ/MCwscHIKQO9icfrZXNycVY=').hexdigest().upper()
    
    return (upai_policy,signature)

def index(request):
    return render_to_response('./index.html')

def list(request):
    return render_to_response('./collection_list.html')

def add(request):
    
    upai_policy , signature = _get_upaiPolicy_Signature();
    return render_to_response('./collection_add.html',{'upai_policy':upai_policy,
                                                       'signature':signature})