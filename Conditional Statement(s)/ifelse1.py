''' Accept a number from the user findout the given number is +ve or -ve '''

n=int(input("Enter a number: "))

#Conditional Statement
if n>=0:
    print("Positive")
else:
    print("Negative")

#Conditional Operator
print("Positive")if n>=0 else print("Negative")
