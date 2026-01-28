'''To print square for the given number'''
import time

n = int(input("Enter a number: "))

for i in range(1, 2):
    time.sleep(0.2)
    print(n, "square =", n * n)

print("============================")
