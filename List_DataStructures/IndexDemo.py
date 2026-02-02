'''L.index(item[,start[,end]])-->int | Value error'''

a=[10,20,10,30,50]
print("List a: ",a)

print("List a: ",a)
pos=a.index(10)
print("Found at: ",pos)

pos=a.index(10,2)
print("Found at: ",pos)

pos=a.index(10,2,5)
print("Found at: ",pos)

pos=a.index(120)
