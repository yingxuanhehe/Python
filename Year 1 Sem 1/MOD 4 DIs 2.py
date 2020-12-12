# Consider a system for storing anonymous grades of each lab class.
# Define a data structure, which can identify individuals in each lab group by an ID number 1-40 (inclusive).
# To identify the person in the entire class you would also need the group name, e,g., ‘FE2’.
# Each corresponding person should have a number between 1-100 (inclusive) to define grade.

grades = {

    'FS1': [45, 75, 25, 96],

    'FS2': [65, 87, 95, 45]

}

print(grades['FS1'][1]) 

