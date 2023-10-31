import random

max = 10
n = random.randint(1, max)
print('Guess the number from 1 to %d' % max)
guess = None
while guess != n:
    guess = int(input('Your try: '))
    if guess > n:
        print('you lose')
      #  break
    if guess < n:
        print('you lose')
      #  break
    if guess == n:
        print("you win the game")
