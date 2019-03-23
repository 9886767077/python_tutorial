import random
random_num = random.randint(1,5)

num = int(input("enter a number between 1 to 5"))

if (num == random_num):
    print("you guessed correctly you won")
    print("Random Number = {}".format(random_num))
else:
    print("sorry you lost")
    print("Random Number = {}".format(random_num))