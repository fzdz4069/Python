# 1. Cleaning a txt file of numbers and punctuation marks, and saving as a new file.
# 2. Using a Python dictionary to count how many times a specific word appears in a book.

def clean_text(file_read, file_write):
    old_file = open(file_read, "r")
    new_file = open(file_write, "w")
    for line in old_file:
        line = line.rstrip()
        for letter in line:
            if letter in "123456789!@#$%^&*()_+-=,./;'[]{}:?><":
                line = line.replace(letter, "")
        new_file.write(line)


def clean_text_dict(filename, query):
    read = open(filename, "r")
    counts = dict()

    for line in read:
        line = line.strip()
        words = line.split()

        for word in words:
            for letter in word:
                if letter in "123456789!@#$%^&*()_+-=,./;'[]{}:?><":
                    word = word.replace(letter, "")
            counts[word] = counts.get(word, 0) + 1

    counts[""] = 0
    print(counts[query])
    read.close()


q = input("Search name: ")
clean_text_dict("Bible.txt", q)
