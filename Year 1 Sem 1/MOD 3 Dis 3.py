#There is a sequence called the Fibonacci sequence.
#The first two numbers in the Fibonacci sequence are both 1, and the third number (as well as the remaining numbers in the sequence) is the sum of the previous two.
#Write a simple Python program to generate this sequence before 1000.  Note: use multiple assignments with a simple while loop to compute.

a= 1

b= 1

while a < 1000:

print(a)

a, b = b, a+b