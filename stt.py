from ibm_cloud_sdk_core import authenticators
from ibm_watson import SpeechToTextV1, speech_to_text_v1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey1 = 'hS59roO4PgEYXAAM2ylR9BTL60lfClcIZAO1ZJav4e5E'
url1 = 'https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/aa6539bd-11dc-4273-a2a9-a3dbca8c2ea7'
#setup service
authenticator = IAMAuthenticator(apikey1)
stt = SpeechToTextV1(authenticator = authenticator)
stt.set_service_url(url1)
# open audio source and convert
#perform conversion
with open('voice.mp3' , 'rb') as f :
    res = stt.recognize(audio=f , content_type='audio/mp3' , model='en-US_NarrowbandModel').get_result()
text = res['results'][0]['alternatives'][0]['transcript']    
with open('output.txt','w') as out :
    out.writelines(text)
