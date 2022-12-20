import sys

script, input_encoding, error = sys.argv

def main(language_file, destination, encoding, errors):
    line = language_file.readline()

    if line:
        destination.write(f"{print_line(line, encoding, errors)}\n")
        return main(language_file, destination, encoding, errors)

def print_line(line, encoding, errors):
    next_language = line.strip()
    return next_language.encode(encoding, errors=errors)

languages = open("languages.txt", encoding="utf-8")

main(languages, open("lang_bytes.txt", 'w'), input_encoding, error)