def get_user_guess() -> int:
    while True:
        try:
            guess = int(input("Please guess a number: "))
        except:
            print("That's not an integer!")
        else:
            return guess