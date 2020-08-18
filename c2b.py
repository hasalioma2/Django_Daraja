import requests
from requests.auth import HTTPBasicAuth

import keys


consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
json_response = r.json()
my_access_token = json_response['access_token']

# print(my_access_token)

access_token = my_access_token

def register_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = { 
    "ShortCode": keys.C2BShortcode,
    "ResponseType": "Completed",
    "ConfirmationURL": "https://fullstackdjango.com/confirmation",
    "ValidationURL": "https://fullstackdjango.com/validation_url",
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

def simulate():

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = { 
        "ShortCode":keys.C2BShortcode,
        "CommandID":"CustomerPayBillOnline",
        "Amount":"1",
        "Msisdn":keys.test_msdin,
        "BillRefNumber":"Pay Internet" 
        }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

simulate()