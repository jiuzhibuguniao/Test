#######################
#js_load_test
#Author:@Rooobins
#Date:2019-01-03
#######################


import json
with open("./Data/test.js") as f:
    js=json.load(f)
    print(js)