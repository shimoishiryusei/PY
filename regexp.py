import re

input = "input2.csv"
FD = open(input,'r')
for line in FD:
    if (re.search(r"^#", line)):
        continue

    line = line.rstrip("\n")
    line = line.rstrip("\r")

    tmp  = line.split(",")
    i = int(tmp[0])
    for j in range(4):
        print("%d 行目: tmp[%d] = %6s" % (i, j, tmp[j]))
FD.close()
