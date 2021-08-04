apikey2 = 'ljzsLnv_mAr_2j8pPINdYh-y-lapheIPtpQ1QjxgdfXp'
url2 = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/7b172819-89ce-42c2-b6fd-3615f1176ba0'
from ibm_cloud_sdk_core import authenticators
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator(apikey2)
tts = TextToSpeechV1(authenticator = authenticator)
tts.set_service_url(url2)
with open('./speech.mp3','wb') as audio_file:
 res= tts.synthesize('hello world', accept='audio/mp3' , voice='en-US_AllisonV3Voice').get_result()
 audio_file.write(res.content)

