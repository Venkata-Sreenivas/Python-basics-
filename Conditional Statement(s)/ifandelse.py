'''Accept marks from the user for 3 subjects print pass if marks>=34 and  else fail'''

m1=int(input("Enter m1: "))
m2=int(input("Enter m2: "))
m3=int(input("Enter m3: "))

if m1>34 and m2>34 and m3>34:
    print("result is: Pass")
else:
    print("Result is: Fail")
