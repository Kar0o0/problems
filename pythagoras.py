#   Write a program that accepts three positive integers
#   as input from the user and prints YES if it is possible
#   to construct a right triangle with the given
#   side lengths, and NO otherwise.

numbers = [int(input()),int(input()),int(input())]
chord = max(numbers)
others = 0
for i in numbers:
    if i == chord:
        continue
    else:
        others += i**2
if others == chord**2:
    print("YES")
else:
    print("NO")