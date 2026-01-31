'''To print

* * *
* *
*
*
* *
* * *

 using nested loop'''

# Upper part
for i in range(3, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower part
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()
