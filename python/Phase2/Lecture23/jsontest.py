#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA

import json

# 将Python数据结构编码为JSON格式。
dictlist = [{'name':'Tom', 'age': 14}, {'name':'Jerry', 'age':13} ]
jsondata = json.dumps(dictlist, sort_keys=True, indent=4, separators=(',', ': '))
print(jsondata)

# 将JSON格式的数据转换为Python对象
jsonstring = '[{"name":"Tom", "age": 14}, {"name":"Jerry", "age":13} ]'
alist = json.loads(jsonstring)
print(alist)





