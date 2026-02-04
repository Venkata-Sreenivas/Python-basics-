'''L.remove(item)'''

lst=[10,20,30,10,20,40,50]
print("List: ",lst)

sno=int(input("Enter Delete No: "))
for i in lst:
    if i==sno:
        lst.remove(i)

print("List: ",lst)
