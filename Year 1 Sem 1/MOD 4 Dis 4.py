# Write a Python program, in the fewest number of lines possible,
# which creates a list of all the square numbers: x2 (where 1<=x<=100) that are divisible by 3.

list = []

for num in range(1, 101):
    if num ** 2 % 3 == 0:
        list.append(num ** 2)

print(list)