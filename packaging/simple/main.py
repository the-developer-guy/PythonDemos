from myui import get_user_guess
from mymath.fake_random import random_die

guess = get_user_guess()
cpu = random_die()
if guess == cpu:
    print("Yes! You guessed right!")
else:
    print("Better luck next time!")
