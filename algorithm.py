from pprint import pprint
import requests

subscription_key = 'key'
assert subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"

key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)

file_object = open('data.txt', 'r')

documents = {'documents' : [
    {'id' : 1, 'language' : 'en', 'text' : file_object.read()}
]}

headers   = {'Ocp-Apim-Subscription-Key': subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()

pprint(key_phrases)
