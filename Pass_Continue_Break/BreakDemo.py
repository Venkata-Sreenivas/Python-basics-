import time
i=1
while i<=10:
    time.sleep(.02)
    if i==6:
        break
    print(i)
    i=i+1
