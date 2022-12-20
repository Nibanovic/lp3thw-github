from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = " ")

source_file = open(input_file)

print_all(source_file)
rewind(source_file)

current_line = 1
print_a_line(current_line, source_file)
current_line += 1
print_a_line(current_line, source_file)