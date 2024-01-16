# https://drive.google.com/drive/folders/13YLxtKExGve6ZlHnDIt4jVkQHf7Yzp53?usp=drive_link

import os

chapters = {'01': 50, '02': 40, '03': 27, '04': 36, '05': 34, '06': 24, '07': 21, '08': 4, '09': 31, '10': 24,
            '11': 22, '12': 25, '13': 29, '14': 36, '15': 10, '16': 13, '17': 10, '18': 42, '19': 150, '20': 31,
            '21': 12, '22': 8, '23': 66, '24': 52, '25': 5, '26': 48, '27': 12, '28': 14, '29': 3, '30': 9, '31': 1,
            '32': 4, '33': 7, '34': 3, '35': 3, '36': 3, '37': 2, '38': 14, '39': 4, '40': 28, '41': 16, '42': 24,
            '43': 21, '44': 28, '45': 16, '46': 16, '47': 13, '48': 6, '49': 6, '50': 4, '51': 4, '52': 5, '53': 3,
            '54': 6, '55': 4, '56': 3, '57': 1, '58': 13, '59': 5, '60': 5, '61': 3, '62': 5, '63': 1, '64': 1,
            '65': 1, '66': 22}


def merge(book):
    n = 1
    while n <= chapters[book]:
        os.system("echo '" + str(n) + "' >> 1879/" + book + ".txt")
        if n < 10:
            os.system("cat -b 1879/" + book + "/0" + str(n) + ".txt >> 1879/" + book + ".txt")
        else:
            os.system("cat -b 1879/" + book + "/" + str(n) + ".txt >> 1879/" + book + ".txt")
        n += 1


for bk in chapters:
    merge(bk)


def merge_books():
    for book in chapters:
        os.system("echo " + book + " >> BG.txt")
        os.system("cat 1879/" + book + ".txt >> BG.txt")


merge_books()

os.system('type BG.txt >> BG.docx')
