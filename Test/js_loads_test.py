#######################
#js_loads_test
#Author:@Rooobins
#Date:2019-01-03
#######################


import json

jsonData = '[{"a":"1","b":2,"c":3,"d":4,"e":5}]'

text = json.loads(jsonData)
print(text)