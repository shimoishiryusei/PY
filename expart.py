import re

input = "template.xlsx"

FD = open(input, "r")
for line in FD:
    line = line.rstrip("\n")
    line = line.rstrip("\r")

    tmp = line.split(",")
    print(tmp)

FD.close()
