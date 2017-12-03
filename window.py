from requests import *
import json
import time
import os

save_path = os.getcwd() + '/data'
int = 0

while True:
    int += 1
    bit = get('https://api.coindesk.com/v1/bpi/currentprice.json', params=None)
    with open(os.path.join(save_path,'data' +str (int) + '.txt'), "w") as outfile:
        json.dump(bit.text, outfile)
        time.sleep(5)