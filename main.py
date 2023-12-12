def read_file(name):
    with open(name) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def letter_count(text):
    letters = {}
    text.lower()
    for i in text:
        letters.update({i : 1})
    return letters

def main():
    file_path = "books/frankenstein.txt"
    book_contents = read_file(file_path)
    print(letter_count(book_contents))


main()