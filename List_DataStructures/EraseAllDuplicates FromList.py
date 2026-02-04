'''L.remove(item)'''

lst=[10,20,30,10,20,40,50]
print("List: ",lst)

lst2=[]

for i in lst:
    if i not in lst2:
        lst2.append(i)

print("Result is: ",lst2)
