def convert(text, file_2, str1, str2):
    file_2.write(text.replace(str(str1), str(str2)))


filename1 = input("file: ")
filename2 = input("new file: ")
file_1 = open(filename1, "r")
file_2 = open(filename2, "w")
text = file_1.read()

str1 = input("replace: ")
str2 = input("replace with: ")

convert(text, file_2, str1, str2)

file_1.close()
file_2.close()
