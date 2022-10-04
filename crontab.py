import os
import sys
import time
import requests
import pandas as pd

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H%M", time.localtime(now)) # year-month-day hour-minute

# request data
data = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
data = data.json() # load data as json
df = pd.DataFrame.from_dict(data) # load into pandas df
df.to_csv('data/covid' + nowStr + '.csv') # save data as .csv locally into data folder


## create a new file in the current working directory
# this saves data in the virtual machine
with open('/home/rima/crontab/covid' + nowStr + '.csv', 'w') as f:
    f.write(str(df)) 



