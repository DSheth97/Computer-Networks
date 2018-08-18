def coun(r):
    one=0
    zero=0
    for i in r:
        if(i=='1'):
            one+=1
        elif(i=='0'):
            zero+=1
    if(one%2==0):
        return '0'
    else:
        return '1'
data = input("Enter your data")
received = input("Enter the data received")
p1=""+'x'
p2=""+'x'
p4=""+'x'
p8=""+'x'

m=p1+p2+data[0:1:1]+p4+data[1:4:]+p8+data[4::]
#print(m)
r =m[0::2]
x= coun(r)
p1=x
m=p1+p2+data[0:1:1]+p4+data[1:4:]+p8+data[4::]
#print(m)
r1=m[1:3:]+m[5:7:]+m[9:11:]
x1= coun(r1)
p2=x1
m=p1+p2+data[0:1:1]+p4+data[1:4:]+p8+data[4::]
#print(m)
r2=m[3:7:]+m[11::]
#print(r2)
x2=coun(r2)
#print(x2)
p4=x2
m=p1+p2+data[0:1:1]+p4+data[1:4:]+p8+data[4::]
#print(m)
r3= m[7::]
x3=coun(r3)
p8=x3
m=p1+p2+data[0:1:1]+p4+data[1:4:]+p8+data[4::]

print("Hamming code is",m)
if(m is received):
    print("Data successfully retrieved")
else:
    print("Error in received data!! The correct data is", m)
'''for i in received:
    if(m[i]==received[i]):
        continue
    else:
        print("Error in received data!! The correct data is ",m)
        break'''






