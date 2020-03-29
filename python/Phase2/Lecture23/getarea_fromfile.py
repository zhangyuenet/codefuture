#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time

try:
    world = {}

    f = open('DXYArea.json' , 'r')
    alist = json.loads(f.read()) #a dict
    results = alist["results"] #a list
    print(len(results))
    for result in results:
        world[result["countryName"]] = result["confirmedCount"]
    print(world)
    print("\r\n =============================== \r\n")
    #sort
    sortlist = []
    for key in world.keys():
        sortlist.append([world[key] , key])
    sortlist.sort(reverse = True)
    world2 = {}
    for item in sortlist:
        world2[item[1]] = item[0]

    print(world2)

except:
    print("Error: Load data failed.")

finally:
    f.close()