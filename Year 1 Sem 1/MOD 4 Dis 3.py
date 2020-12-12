# Write a Python program that will check which class has the highest average score and the highest maximum score.
def get_scores():
    list_scores = []

    for scores in range(10):
        value = int(input("Enter score: "))

        list_scores.append(value)

    return list_scores


def get_total(value_list):
    total = 0

    for num in value_list:
        total += num

    return total


scores = get_scores()

total = get_total(scores)

average = total / len(scores)

my_list = [get_scores]

print('The lowest score is:', min(scores))

print('The highest score is:', max(scores))

print('The average is:', average)
