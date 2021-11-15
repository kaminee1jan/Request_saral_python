# write a program ro call url
# `requests` module use kar kar,
# -# [yeh](http://saral.navgurukul.org/api/courses) `API Endpoint` ya `URL` call kar kar
# yeh data `courses.json` file mei store karna hai.
 
#when we do request question firstly we have to write pip install request in terminal

import requests
import json

url = ' https://saral.navgurukul.org/api/courses'
response = requests.get(url)          
k = json.loads(response.text)
print(k)


