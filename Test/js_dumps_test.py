#######################
#js_dumps_test
#Author:@Rooobins
#Date:2019-01-03
#######################

import json

ls=[{"name":"wangkai","age":27},{"name":"wangzhen","age":25}]

js=json.dumps(ls,indent=4,separators=(",",":"),sort_keys=True)

print(js)




# ls=[{"name":"wangkai","age":27},{"name":"wangzhen","age":25}]
#
# js=json.dumps(ls)
#
# print(js)