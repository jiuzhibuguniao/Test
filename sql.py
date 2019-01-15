import pymysql
import time


def storeDataToMysql():
    test = pymysql.connect(host='39.108.100.28', user='Rooobins', password='19910909kai', db='spiderData', port=3306)
    cursor=test.cursor()
    create_table="""set @sql_create_table=concat('CREATE TABLE IF NOT EXISTS operrecord_',date_format(NOW(),'%y%m%d%H'),
"(
    `distId` varchar(50) primary key,`distX` double,`distY` double,`distNum` int,`distance` varchar(50),`bikeIds` varchar(50),`biketype` varchar(50),`type` varchar(50),`boundary` varchar(50)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8");"""
    create_prepare="""PREPARE sql_create_table FROM @sql_create_table;"""
    create_execute="""EXECUTE sql_create_table;"""
    cursor.execute(create_table)
    cursor.execute(create_prepare)
    cursor.execute(create_execute)
    test.commit()
    cursor.close()



storeDataToMysql()