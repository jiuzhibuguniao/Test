##############################
#Author:@Rooobins
#Date:2018-12-20
##############################


istr=input(">>")
re_istr=''


i=0
while i<len(istr):
    k=1
    if i+k!=len(istr):
        while (istr[i]==istr[i+k])  :
            k=k+1
            if i+k<len(istr) :continue;break
        if k==1:
            re_istr+=istr[i]
        else:
            re_istr=str(k)+istr[i]
        i=i+k
    else:
        re_istr+=istr[i]
        i=i+1



print(re_istr)