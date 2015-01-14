from django.shortcuts import render,redirect
import settings
from django.http import HttpResponse

import urllib,json,requests
# Create your views here.
def index(request):
    return redirect(settings.oauth['auth_uri']+"?"+\
        urllib.urlencode(settings.oauth['parameters']))


def oauth2callback(request):
    return HttpResponse(json.dumps(request.GET.items()),content_type='application/json')


