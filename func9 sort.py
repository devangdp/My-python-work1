v1=int(input('Enter v1:'))
v2=int(input('Enter v2:'))
v3=int(input('Enter v3:'))
a=[]
def order_num():
    a.append(v1)
    a.append(v2)
    a.append(v3)
    a.sort()
    print(a)

order_num()