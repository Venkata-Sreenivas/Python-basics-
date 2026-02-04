'''Ways to define Tuple'''

a=()
print("Data is: ",a)
print("=============================")

b=(10,12.12,"Sreenivas",21,"Venkata",None)
print("Data is: ",b)
print("=============================")

c=(10,)
print("Type is: ",type(c))
print("Data is: ",c)
print("=============================")

d=10,12.12,"Sreenivas" #packing | tuple
print("Type is: ",type(d))
print("Data is: ",d)
print("=============================")


'''tuple()-->tuple'''
e=tuple()
print("Data is: ",e)
print("=============================")

'''tupe(iterable)-->tuple'''
lst=[10,20,30,40]
print("List: ",lst)
f=tuple(lst)
print("Data is: ",f)
print("=============================")

s={10,20,30,40,10}
print("Set: ",s)
g=tuple(s)
print("Data is: ",g)
print("=============================")

st="Welcome" #str is the collection of char sequence
print("String: ",st)
h=tuple(st)
print("Data is: ",h)
print("=============================")

stu={"Sno":101,"Sname":"Sreenivas","Sage":21}
print("Stu is: ",stu)
i=tuple(stu)
print("Data is: ",i)
