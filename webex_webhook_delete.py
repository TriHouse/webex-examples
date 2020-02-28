#!/usr/bin/env python
'''
Example of how to clean up the Webex Webhooks.
204 http response from the on successful delete
'''
import json
import requests
import logging

WEBEX_BOT_TOKEN ='WEBEX_TOKEN'
WEBEX_API_URL = 'https://api.ciscospark.com/v1/'

def send_webex_api(type, api_type, data, files = False): #post/get/put, messages/rooms, data
    url = WEBEX_API_URL + api_type
    headers = {'Authorization': 'Bearer ' +  WEBEX_BOT_TOKEN }
    r = requests.request(type, url, headers=headers, data=data)       
    return r

data = {} # no data required
my_api = send_webex_api ('get', 'webhooks', data)
data = my_api.json()

for wh in data["items"]:
    my_api = send_webex_api ('delete', 'webhooks/' + wh["id"], data)
    print (f'{my_api.status_code}" -  {wh["id"]}')