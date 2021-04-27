input = "input.csv"

FD = open(input, "r")

for line in FD:
    line = line.rstrip("\n")
    line = line.rstrip("\r")

    tmp = line.split(",")
    i = int(tmp[0])
    j = tmp[3]
    if i % 2 == 0:
        print("%d行目:          4列目: %6s\n" %(i, j))
    else:
        print("%d行目: 2列目+ 3列目: %.5f\n" %(i, float(tmp[1])+float(tmp[2])))
FD.close()
