import requests,unicodedata,base64, json
import settings

NORMAL_FORM = 'NFKD'

class OauthBackend:
    urls={}
    def __init__(self):
        self.urls=self.getUrls()
    
    def getUrls(self):
        r=requests.post(settings.oauth['discovery_document'])
        return r.json()      
    
    def getToken(self,code):
        data={'code':code,\
              'client_id':settings.oauth['parameters']['client_id'],
              'client_secret':settings.oauth['client_secret'],
              'redirect_uri':settings.oauth['parameters']['redirect_uri'],
              'grant_type':'authorization_code'}
        r=requests.post(self.urls['token_endpoint'],data=data)
        return r.json()
    
    def decode(self,token):
        [header,payload,signature]=token.split(".")
        payload=unicodedata.normalize(NORMAL_FORM,payload).encode('ascii','ignore')
        payload+='='*(4-(len(payload)%4))
        decoded_payload = base64.urlsafe_b64decode(payload)
        return json.loads(decoded_payload)['email']
