'''To print

1111
2222
3333

block'''

import time

o=4

for o in range(1,4):
    for i in range(1,5):
        time.sleep(.02)
        print(o,end=' ')
    print("")
