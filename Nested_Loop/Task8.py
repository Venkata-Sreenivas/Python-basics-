'''To print

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1


 using nested loop'''

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()
