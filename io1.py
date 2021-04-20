input = "input.csv"
FD = open(input, "r")
for line in FD:
    line = line.rstrip("\n")
    line = line.rstrip("\r")

    tmp = line.split(",")
    i = int(tmp[0])
    for j in range(4):
        print("%d行目: tmp[%d] = %6s" %(i, j, tmp[j]))
FD.close()
