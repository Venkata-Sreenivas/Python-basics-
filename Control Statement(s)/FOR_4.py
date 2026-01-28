'''To print table for the given number'''
import time

n=int(input("Enter a number: "))

for i in range(1,11):
    time.sleep(.02)
    print(n,"x",i,"=",n*i)

print("===================================")

'''To print reverse table'''
for i in range(10,0,-1):
    time.sleep(.02)
    print(n,"x",i,"=",n*i)
