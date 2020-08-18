import requests

from datetime import datetime
import keys
print (datetime.now())

# 2020-08-18 13:50:57.415621

def lipa_na_mpesa():
    access_token = "Access-Token"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": keys.business_shortCode,
    "Password": " ",
    "Timestamp": " ",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": keys.PhoneNumber,
    "PartyB": keys.business_shortCode,
    "PhoneNumber": keys.PhoneNumber,
    "CallBackURL": "https://fullstackdjango.com/callback",
    "AccountReference": "1234567",
    "TransactionDesc": "test Mpesa"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

# lipa_na_mpesa()