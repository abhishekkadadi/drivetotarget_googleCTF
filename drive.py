import re
import requests as req
import time
import random
url = 'https://drivetothetarget.web.ctfcompetition.com/'
url_data=req.get(url);

lat,lon=1,0
while True:
    values=re.findall('value="(.*?)"',url_data.text);
    parameters={}
    parameters['lat']=float(values[0])-lat*0.00004
    parameters['lon'] = float(values[1]) - lon * 0.00004
    parameters['token'] = values[2]

    url_data = req.get(url, params=parameters)
    print(url_data.text)
    flag=re.findall(r'CTF{.*?}',url_data.text)
    if flag:
        print(flag[0])
        break
    if 'You are getting away' in url_data.text:  # If we are moving away...
        while True:  # Change the direction to a random (non-zero) one.
            lat, lon = random.choice([-1, 0, 1]), random.choice([-1, 0, 1])
            if lat * lon != 0:
                break
