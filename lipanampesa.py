import requests
import base64

from datetime import datetime
import keys

from requests.auth import HTTPBasicAuth



formatted_time = datetime.now().strftime("%Y%m%d%H%M%S")

data_to_encode = keys.LNM_Short_code + keys.LNM_Passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
decoded_pass = encoded_string.decode('utf-8')


consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
json_response = r.json()
my_access_token = json_response['access_token']

# print (my_access_token)


def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": keys.LNM_Short_code,
    "Password": decoded_pass,
    "Timestamp": formatted_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": keys.PhoneNumber,
    "PartyB": keys.LNM_Short_code,
    "PhoneNumber": keys.PhoneNumber,
    "CallBackURL": "https://fullstackdjango.com/callback",
    "AccountReference": "1234567",
    "TransactionDesc": "test Mpesa"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

lipa_na_mpesa()