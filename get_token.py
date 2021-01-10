#!/usr/bin/env python3.8

import requests
import base64
from credentials import username, password
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_token():
    creds = f'{username}:{password}'
    creds_bytes = creds.encode('ascii')
    encoded_creds = base64.b64encode(creds_bytes).decode('ascii')
    auth = f'Basic {encoded_creds}'    

    url = 'https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/auth/generatetoken'
    headers = {
    'Content-Type': 'application/xml',
    'Authorization': auth,
    }
    
    print(url)
    print(headers)

    response = requests.post(url, headers=headers, verify=False)
    response_headers = response.headers

    token = response_headers['X-auth-access-token']
    UUID = response_headers['DOMAIN_UUID']

    result = {'token': token, 'uuid': UUID}

    return result



if __name__ == '__main__':
    result = get_token()
    print(result)
