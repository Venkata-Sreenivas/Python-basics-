'''To print Possible Values from list'''

#Unpacking

lst=[10,"Sreenivas","Hyd"]
print("List: ",lst)

'''
a=lst[0]
b=lst[1]
c=lst[2] '''

#a,b=lst ValueError
a,b,c=lst

print(a,b,c,sep='-')
print("================================")

x=lst#ref.copy
print("List lst: ",lst)
print("List x: ",x)

