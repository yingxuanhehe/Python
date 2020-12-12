import random

def game():
    random_number = [random.randint(0, 9) for n in range(4)]
    print("Solution:", random_number)


    while True:
        guess = [int(i) for i in str(input("Please guess a 4-digit number: "))]

        if guess == random_number:
            print("-----Congratulations! You have won the game!-----")
            break

        else:
            cow = 0
            bull = 0

            for i in range(4):
                if guess[i] == random_number[i]:
                    bull += 1

                elif guess[i] in random_number:
                    cow += 1

            print(bull, "A (Bulls)  ", cow, "B(Cows)")


game()
