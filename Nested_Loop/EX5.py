'''To print

12345
12345
12345
12345

block'''
import time
for o in range(1,5):
    for i in range(1,6):
        time.sleep(.02)
        print(i,end=' ')
    print(" ")
