i = 2
j = 2
incorr_count = 0
while i <= 10 and j <= 10:
    try:
        res = int(input(str(i) + " x " + str(j) + " = "))
    except ValueError as err:
        print(err)
    if i * j == res:
        print("correct")
    else:
        print("incorrect\n" + str(i) + " x " + str(j) + " = " + str(i * j))
        incorr_count += 1
    i += 1
    if i == 10:
        res = int(input(str(i) + " x " + str(j) + " = "))
        i = 2
        j += 1
if incorr_count < 10:
    print("good")
else:
    print("bad")
