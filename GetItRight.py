import random
num = eval(input("Please guess the random number :"))
guess = random.randint(0, 20)
if guess < num:
    print("Your guess is too low")
else:
    print("Your guess is too high")
