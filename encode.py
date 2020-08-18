
import keys
import base64

def generate_password(formatted_time):  
    data_to_encode = keys.LNM_Short_code + keys.LNM_Passkey + formatted_time
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_pass = encoded_string.decode('utf-8')

    return decoded_pass