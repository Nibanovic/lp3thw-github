from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit ^C")
print("If you do want that, hit ENTER")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Now give me three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")


print("And finally, we close the file.")
target.close()