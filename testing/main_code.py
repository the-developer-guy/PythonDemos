import time

def is_even(number: int) -> bool:
    match number:
        case int():
            return number % 2 == 0
        case _:
            raise TypeError("Unsupported type!")

def untested() -> int:
    now = int(time.time())
    if now % 100 == 0:
        raise Exception("Unlucky day!")
    else:
        print("Hello, dear user!")


if __name__ == "__main__":
    num = int(input("Please, give a number!"))
    print(is_even(num))
    untested()
