from django.shortcuts import render,redirect
import settings
from django.http import HttpResponse
from django.utils.crypto import get_random_string
import urllib,json,requests
# Create your views here.
def index(request):
    state=get_random_string(length=32)
    parameters=settings.oauth['parameters'].copy()
    parameters['state']=state
    request.session['state']=state
    return redirect(settings.oauth['auth_uri']+"?"+\
        urllib.urlencode(parameters))


def oauth2callback(request):
    if request.session.get('state','')==request.GET['state']:
        return HttpResponse(json.dumps(request.GET.items()),content_type='application/json')
    else:
        return HttpResponse(json.dumps({"error":"aa"}))


