def read_file(name):
    with open(name) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def letter_count(text):
    letters = {}
    text = text.lower()
    for i in text:
        if i in letters:
            letters.update({i : letters[i] + 1})
        else:
            letters.update({i : 1})
    return letters

def aggregate_letter_count(letterDict, filePath, contents):
    print(f"--- Begin reprot of {filePath} ---")
    print(word_count(contents), "words found in the document\n")
    sortedDict = []
    for i, j in letterDict.items():
        sortedDict.append((j, i))
    finalList = []
    for i in sortedDict:
        if i[1].isalpha():
            finalList.append(i)
    finalList = sorted(finalList, reverse=True)
    for i in finalList:
        print(f"The \'{i[1]}\' character was found {i[0]} times")
    print("--- End report ---\n")

def main():
    file_path = "books/frankenstein.txt"
    book_contents = read_file(file_path)
    aggregate_letter_count(letter_count(book_contents), file_path, book_contents)


main()