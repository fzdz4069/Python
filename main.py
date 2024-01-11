import os

n = 1
while n <= 9:
    os.system("echo '-----' >> 1879/01-gen/0" + str(n) + ".txt")
    os.system('cat 1879/01-gen/0' + str(n) + '.txt >> 1879/01-gen/temp.txt')
    n += 1
