formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Svaki dan",
    "Ustajem se",
    "Otvorim oči",
    "I skočim"
))

#-------

days = "Pon Uto Sri Čet"
months = "Sij\nVelj\nOžu\nTrav"

print("Evo dana: ", days)
print("Evo mjeseci:", months)

print('''
There is something going on there.
With the three double-quotes
We'll be able to type as much as we like,
even 4 or 5 or 6 lines of code
''')