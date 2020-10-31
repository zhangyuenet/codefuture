#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time

url = 'https://lab.isaaclin.cn/nCoV/api/area?latest=1'
data = requests.get(url).text

world = {}

alist = json.loads(data) #a dict
results = alist["results"] #a list
print(len(results))
for result in results:
    world[result["countryName"]] = result["confirmedCount"]
#sort
sortlist = []
for key in world.keys():
    sortlist.append([world[key] , key])
sortlist.sort(reverse = True)
world2 = {}
for item in sortlist:
    world2[item[1]] = item[0]

print(world2)