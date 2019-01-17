import pymssql
conn=pymssql.connect(host='ROOOBINS-PC',user='sa',password='w*K19910909',database='Student')
'''
 如果和本机数据库交互，只需修改链接字符串
 conn=pymssql.connect(host='.',database='Michael')
 '''
cur=conn.cursor()

cur.execute('select top 2 * from [dbo].[teacher]')
#如果update/delete/insert记得要conn.commit()
#否则数据库事务无法提交
print (cur.fetchall())

cur.close()

conn.close()