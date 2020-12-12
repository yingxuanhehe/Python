#When choosing a password for online accounts, there are typically certain requirements for the strength of the password. Develop a Python program for testing if a string satisfies some appropriate criteria for a strong password. It’s up to you to define the requirements.

#Minimum 8 characters.

#The alphabets must be between [a-z]

#At least one alphabet should be of Upper Case [A-Z]

#At least 1 number or digit between [0-9].

#At least 1 character from [ _ or @ or $ or *]

LENGTH = 10

upCase = False

lowCase = False

digit = False

password = input("Input your password:")

for char in password:
    if char.isupper():
        upCase = True
    if char.islower():
        lowCase = True
    if char.isdigit():
        digit = True

length = len(password)

strong = upCase and lowCase and digit and length > LENGTH

if strong:
    print("Your password is strong.")

else:
    print("Password is weak.")
