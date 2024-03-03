from collections.abc import Iterable

class Bucket:
    def __init__(self) -> None:
        self.storage = []

    def add(self, item):
        self.storage.append(item)
    
    def __iter__(self):
        self.iterator_index = 0
        return self
    
    def __next__(self):
        try:
            retval = self.storage[self.iterator_index] 
        except IndexError:
            raise StopIteration
        else:
            self.iterator_index += 1
            return retval

if __name__ == "__main__":
    bucket = Bucket()
    lucky_number = 9001

    bucket.add("fish")
    bucket.add(lucky_number)

    for item in bucket:
        print(item)
    
    print(f"Is bucket iterable? {isinstance(bucket, Iterable)}")
    print(f"Is bucket REALLY an iterable? {issubclass(Bucket, Iterable)}")

    match bucket:
        case Iterable():
            print("Yes, match-case thinks our bucket is iterable!")
        case _:
            print("Just a bucket.")
    
    match lucky_number:
        case Iterable():
            print("What? Integers are iterable too?")
        case _:
            print("Just a number.")