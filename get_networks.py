#!/usr/bin/env python3.8
import requests
from get_token import get_token

def get_networks(token, uuid):
    url = f'https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/{uuid}/object/networks'
    headers = {'X-auth-access-token': token}

    print(url)
    print(headers)

    result = requests.get(url, headers=headers, verify=False)
    print('{:10s} | {:10s}'.format('Type', 'Name'))
    print(25*'-')
    for network in result.json()['items']:
        net_type = network['type']
        name = network['name']
        print(f'{net_type:10} | {name:10}')
    

if __name__ == '__main__':
    result = get_token()
    get_networks(result['token'], result['uuid'])
