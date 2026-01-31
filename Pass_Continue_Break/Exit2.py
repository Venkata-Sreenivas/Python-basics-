import sys
import time

i=1
while i<=10:
    time.sleep(.02)
    if i==6:
        sys.exit()
    print(i)
    i=i+1

print("Have a nice day")
    

