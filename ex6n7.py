types_of_people = 10
x = f"there are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# -----

print("Mary had a little lamb")
print("Its fleece was as white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"

print(end1 + end2 + end3)
print(end4 + end5 + end6)