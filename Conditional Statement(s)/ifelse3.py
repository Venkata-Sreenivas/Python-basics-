'''Accept marks from the user print pass if marks>=34 else fail'''

marks=int(input("Enter marks: "))

#Conditional Statement
if marks>=34:
    print("Pass")
else:
    print("Fail")

#Conditional Operator
print("Pass") if marks>=34 else print("Fail")
