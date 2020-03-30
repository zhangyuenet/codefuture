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
    #sort在这里对world进行排序
    #world是一个dict类型的对象。排序的算法可以参考sorttest.py


except:
    print("Error: Load data failed.")

finally:
    f.close()