import requests
import os
import json

def send_sms():
    """Read More
    https://www.multitexter.com/developers
    """
    response = ""    
    API_KEY= 'c493e9d6-bd8d-11ec-9c12-0200cd936042'
    phone_number = '9798565542'
    otp = "126456"

    if otp is None or phone_number is None:
        raise Exception("Phone Number cannot be Null")
    url = f"https://2factor.in/API/V1/{API_KEY}/SMS/+91{phone_number}/{otp}"
    r = requests.post(url)
    response = r.json()
    print(response)

    if response == '':
        return False

    status = response.get('Status')
    print(status)
    
    if status == 'Success':
        return True
    else:
        return False

send_sms()