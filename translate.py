def translate(phrase_1):
    translation = ""
    for letter in phrase_1:
        if letter.lower() == "q":
            translation = translation + "0"
        elif letter.lower() == "a":
            translation = translation + "1"
        elif letter.lower() == "z":
            translation = translation + "2"
        elif letter.lower() == "w":
            translation = translation + "3"
        elif letter.lower() == "s":
            translation = translation + "4"
        elif letter.lower() == "x":
            translation = translation + "5"
        elif letter.lower() == "e":
            translation = translation + "6"
        elif letter.lower() == "d":
            translation = translation + "7"
        elif letter.lower() == "c":
            translation = translation + "8"
        elif letter.lower() == " ":
            translation = translation + "9"
        else:
            translation = translation + letter
    return translation

new_file = open("python write.txt", "w")
new_file.write(translate(input("phrase 1: ")))
new_file.close()

code = {
    0: "q",
    1: "a",
    2: "z",
    3: "w",
    4: "s",
    5: "x",
    6: "e",
    7: "d",
    8: "c",
    9: " "}

def translate_back(phrase_2):
    translation = ""
    for letter in phrase_2:
        if letter in ("0123456789"):
            translation = translation + str(code.get(int(letter)))
        else:
            translation = translation + letter
    return translation

new_file = open("python write.txt", "a")
new_file.write("\n" + translate_back(input("phrase 2: ")))
new_file.close()
