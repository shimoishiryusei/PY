input = "input.csv"
output = "output.txt"
FDI = open(input, "r")

FDO = open(output, "w")
for line in FDI:
    line = line.rstrip("\n")
    line = line.rstrip("\r")

    tmp = line.split(",")
    i = int(tmp[0])
    for j in range(4):
        FDO.write("%d行目 : tmp[%d] = %6s\n" % (i, j, tmp[j])) 
FDI.close()
FDO.close()
