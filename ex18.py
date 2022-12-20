def print_two(*args):
    arg1, arg2 = args
    print(f"i got {arg1} and {arg2} as inputs.")

def print_two_again(arg1, arg2):
    print(f"i got {arg1} and {arg2} as inputs.")

def print_one(arg1):
    print(f"argument: {arg1}")

def print_none():
    print("I got nothing.")

print_two("Nikola", "Banović")
print_two_again("Nikola", "Banović")
print_one("First!")
print_none()