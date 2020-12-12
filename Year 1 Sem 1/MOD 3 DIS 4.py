#Write a Python program that reads an integer from the user, which is the width of the pattern below, and then prints out the pattern. Suggestion: use nested for loops.  Hint: print("*",end=""). 

n = int(input("Please enter pattern width:"))

for i in range(1, n+1):

    for j in range(1, i):
        print("*", end=" ")

    print("*")

for i in range(n - 1, 0, -1):
    for j in range(i):
        print('* ', end="")

    print('')