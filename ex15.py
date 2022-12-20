from sys import argv

script, filename = argv

txt = open(filename)

print("Your file is ", filename, ":")
print(txt.read())
print(f"from script {script}")

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()