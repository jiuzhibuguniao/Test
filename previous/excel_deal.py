#################################
#excel_deal
#Author:@Rooobins
#Date:2018-12-17
#################################


import xlrd
import xdrlib,sys
import xlwt



def open_excel(file):
    data=xlrd.open_workbook(file)
    return data



def deal_excel(file, colnameindex=0, by_name=u'IPC'):
    data_end=[]
    data = open_excel(file) #打开excel文件
    table = data.sheet_by_name(by_name) #根据sheet名字来获取excel中的sheet
    nrows = table.nrows #行数
    colnames = table.row_values(colnameindex) #某一行数据
    list =[] #装读取结果的序列
    for rownum in range(0, nrows): #遍历每一行的内容
         row = table.row_values(rownum) #根据行号获取行
         if row: #如果行存在
             app = [] #一行的内容
             for i in range(len(colnames)): #一列列地读取行的内容
                app.append(row[i])
             list.append(app) #装载数据
    for line in list:
        currData=line[0].strip("\n").split("\n")
        for line_currData in currData:
            data_end.append(line_currData)
    return data_end



#写Excel
def write_excel(data):
    f=xlwt.Workbook()
    sheet1=f.add_sheet("Test",cell_overwrite_ok=True)
    # for row in data:
    #     # for i in range(0,len(row)):
    #         # for j in range(0,len(row[i])):
    #         #     sheet1.write(i,j,row[i][j])
    #     sheet1.write(data.index(row),0,row)
    #
    for i in range(len(data)):
        sheet1.write(i,0,data[i])
    f.save("C:\\Users\\Rooobins\\Desktop\\one.xls")



def main():
    file="C:\\Users\\Rooobins\\Desktop\\2010-2017.xlsx"
    ll=deal_excel(file)
    ll_space=[i for i in range(len(ll)) if ll[i]==""]
    print(ll)
    print(ll_space)
    print(len(ll))
    write_excel(ll)



if __name__=="__main__":
    main()