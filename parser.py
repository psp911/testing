#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import json, requests
from pprint import pprint

#url = 'https://etc.ethermine.org/api/2760fb878e406d24b76e4fa952f9d554fa96d2ba/:2760fb878e406d24b76e4fa952f9d554fa96d2ba/dashboard'

url = 'https://api-etc.ethermine.org/poolStats'

url = 'https://api-etc.ethermine.org/miner/:0x2760fb878e406d24b76e4fa952f9d554fa96d2ba/dashboard'

#url ='https://etc.ethermine.org/miners/2760fb878e406d24b76e4fa952f9d554fa96d2ba/dashboard'

resp = requests.get(url=url)
if resp.status_code == 200:
    print('Success!')
elif resp.status_code == 404:
    print('Not Found.')

print (resp.text)

print("\n\n\n")

d={}
d=resp.text

data = json.loads(d)

#data=d.json()

print(data['data']['workers'][0]['worker'])
print(data['data']['workers'][1]['worker'])
lenList=len(data['data']['workers'])
print(data['data']['workers'][lenList-1]['worker'])

a_dict = data['data']['workers']
#keys = a_dict.worker()
 
#keys = sorted(keys)
for key in a_dict:
    print(key['worker'], round(key['currentHashrate']/1000000,2))

#print(json.dumps(resp.text, sort_keys=True, indent=4))


