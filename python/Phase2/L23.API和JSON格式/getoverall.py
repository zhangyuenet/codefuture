#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time

url = 'https://lab.isaaclin.cn/nCoV/api/overall'
data = requests.get(url).text
#print(data)

alist = json.loads(data) #a dict
results = alist["results"] #a list
result = results[0] # a dict

localtime = time.localtime(result["updateTime"] / 1000)
dt = time.strftime("%Y-%m-%d",localtime)

print("总确诊数：%s, 日期：%s" % (result["confirmedCount"], dt))




