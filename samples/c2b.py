import requests
from requests.auth import HTTPBasicAuth
from access_token import generate_token
import keys



access_token = generate_token()

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

    headers = {"Authorization": "Bearer %s" % access_token}

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