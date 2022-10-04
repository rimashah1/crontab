import os
import sys
import time
import requests

import os 
import sys
import time

# request data
df = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
df = df.json()

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
df.to_csv('/home/rima/crontab/Covid' + nowStr + '.csv')



