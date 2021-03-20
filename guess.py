import random

def Guess_number():
    random_number = random.randint(1 , 10)
    guess = 0

    while guess != random_number:
        guess = int(input("Guess the number between 1 to 10:-\n"))

        if guess > random_number:
            print("Sorry It's too high , try again")

        elif guess < random_number:
            print("Sorry It's too low  , try again")

        else:
            print(f"Congrats You just Guess the correct number that's {random_number}")

if __name__ == "__main__":
    name = input("Please Enter your name here:-\n")
    print(f"-----Welcome {name} just play and enjoy the game----")
    print("\n")
    Guess_number()
