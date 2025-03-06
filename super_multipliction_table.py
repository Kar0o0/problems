# Write a program that takes n as input and prints the multiplication table from 1 to n.

n = int(input())

for i in range(1, n + 1):
    for f in range(1, n + 1):
        print(f * i, end=" ")
    print()
