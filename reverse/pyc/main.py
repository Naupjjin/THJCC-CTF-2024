from FLAG import FLAG
from Crypto.Util.number import bytes_to_long 

def xor1(flag):
    return flag ^ 124789

def xor2(flag):
    return flag ^ 487531

def xor3(flag):
    return flag ^ 784523

def xor4(flag):
    return flag ^ 642871

def xor5(flag):
    return flag ^ 474745

flag=bytes_to_long(FLAG)


count = 0
count +=1
if count == 1:
    flag=xor1(flag)
    count +=2

    if count == 3:
        flag=xor2(flag)
        count+=1

    if count == 4:
        flag=xor3(flag)
        count-=2
    else:
        flag=xor2(flag)
        count+=1

else:
    flag=xor3(flag)
    count+=5

if count==2:
    flag=xor4(flag)

elif count==6:
    flag=xor5(flag)
    
print(flag)

