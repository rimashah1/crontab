import os
import sys
import time
import requests

# request data
df = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
df = df.json()

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open('/home/rima/crontab/Covid' + nowStr + '.txt', 'w') as f:
    f.write(str(df))



