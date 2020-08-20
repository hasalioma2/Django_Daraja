import requests
import keys
from encode import generate_password
from utils import get_timestamp
from access_token import generate_token

def lipa_na_mpesa():
    
    formatted_time = get_timestamp()
    decoded_pass = generate_password(formatted_time)
    access_token = generate_token()
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
    "CallBackURL": "https://692e842ae4a1.ngrok.io/api/payments/lnm/",
    "AccountReference": "1234567",
    "TransactionDesc": "test Mpesa"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

lipa_na_mpesa()