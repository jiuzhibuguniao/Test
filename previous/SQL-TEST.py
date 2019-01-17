import pymssql

conn=pymssql.connect(host='192.168.179.1',user='sa',password='w*K19910909',database='Test')

cur=conn.cursor()

sql="select * from [Test].[dbo].[PeopleInfo]"

cur.execute(sql)

print(cur.fetchall())

cur.close()

conn.close()