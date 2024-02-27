import sys

print(f"We have {len(sys.argv)} argument(s)!")
print(f"The first is always the file path, see? {sys.argv[0]}")

print("All the arguments:")
for arg in sys.argv:
    print(f"- {arg}")
