import re

input = "data1.csv"
err_max = 2e-6

ni = 100
nj = 9

array = [[0 for i in range(ni)] for j in range(nj)]

FD = open(input, "r")
nd = 0;
for line in FD:
    if (re.search(r"^#", line)):
        continue
    line = line.rstrip("\n")
    line = line.rstrip("\r")

    tmp = line.split(",")
    for j in range(nj):
        array[j][nd] = float(tmp[j])
    nd += 1
FD.close()

for i in range(nd):
    T = array[0][i]
    rho = array[1][i]
    R = array[6][i]
    err = array[7][i]

    if (err > err_max):
        print("###", end='')
    print("%7.2f %11.4e %11.4e %11.4e" %(T, rho, R, err))
