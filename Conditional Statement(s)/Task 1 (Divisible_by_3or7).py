''' Accept a number from the user find out the given number is divisble by 3 or 7 '''

n=int(input("Enter a Number: "))

#Conditional Statement 
if n%3==0 or n%7==0:
    print("The Number is divisible by 3 or 7")
else:
    print("The number is NOT divisible by 3 or 7")

#Conditional Operator
print("The Number is divisible by 3 or 7") if n%3==0 or n%7==0 else print("The number is NOT divisible by 3 or 7")
