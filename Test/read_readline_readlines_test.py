##################
#read_test
#Author:@Rooobins
#Date:2019-01-03
##################



with open("./Data/read_test.txt",'r',encoding="UTF-8") as f:
    f.__next__()
    f.__next__()
    f_read=f.read()
    f_readline=f.readline()
    f_readlines=f.readlines()
    print(f_read)
    print(f_read[8])
    print(f_read.split("\n"))
    print(type(f_read))
    print("+++++++++++++++++++++++++++")
    print(f_readline)
    print(type(f_readline))
    print("+++++++++++++++++++++++++++")
    print(f_readlines)
    print(type(f_readlines))
    f.close()
