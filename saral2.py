# - `courses.json` file padh kar
# - aapko iss object ko ek json argument mei load karna hai
# - uss json object ko parse kar kar
# - aapko saare courses ki list print karni hai, jaise

import requests
import json

url = ' http://saral.navgurukul.org/api/courses'
response = requests.get(url)           
k = json.loads(response.text)
for i in k["availableCourses"]:
    print(i["name"])

