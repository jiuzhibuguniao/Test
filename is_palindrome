import math

def number():
    n=0
    yield 0
    while True:
        n=n+1
        yield n


def select_number(n):
    N=str(n)
    s=1
    for i in range(math.ceil(len(N)/2)):
        if N[i]==N[len(N)-1-i]:
            s=(s and 1)
        else:
            s=(s and 0)
    if s:
        return n
    # else:
    #     return

all_number_select=filter(select_number,number())

# print(list(all_number_select))

for i in all_number_select:
    if i<=200:
        print(i)
    else:
        break
