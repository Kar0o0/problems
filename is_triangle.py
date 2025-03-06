# Input:
# The first line of input contains three numbers that indicate the degree of the 3 angles.
# It is guaranteed that all 3 input numbers will be integers, non-negative, and smaller than 360.
# Output:
# In the only output line, if we could construct a triangle with these 3 angles, print the statement Yes, otherwise print the statement No.




numbers = list(map(int, input().split()))
if sum(numbers) == 180:
    if 0 not in numbers:
        print("Yes")
    else:
        print("No")
else:
    print("No")