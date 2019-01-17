#############################
#write_writeliens_test
#Author:@Rooobins
#Date:2019-01-03
#############################

ls=["wangkai\n","wangzhen\n","fenyang\n","zhengyang\n","henan\n","shanxi\n","taiyuan\n","zhengzhou\n"]
with open("./Data/write_writelines_test.txt","w+",encoding="UTF-8") as f:
    f.writelines(ls)
    f.write("successfully")
    f.close()