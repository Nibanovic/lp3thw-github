class Other:
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child:

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD before OTHER altered()")
        self.other.altered()
        print("CHILD after OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

# inheritance VS composition -> when to use which?
#
# avoid multiple inheritance, it is too complex
# INHERITANCE only when there are clearly related reusable pieces of
# code that fit under a single common concept
#
# COMPOSITION to package code into modules that are used in many
# different unrelated places and situations


