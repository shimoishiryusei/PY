import matplotlib.pyplot as plt
import re

input = ["data1.csv", "data2.csv", "data3.csv"]
output = ["data1.txt", "data2.txt", "data3.txt"]
err_max = 2e-6

ni = 100
nj = 9

for in_file, out_file in zip(input, output):
    array = [[0 for i in range(ni)] for j in range(nj)]

    FDI = open(in_file, "r")
    FDO = open(out_file, "w")
    nd = 0;
    x = []
    y = []

    for line in FDI:
        if (re.search(r"^#", line)):
            continue
        line = line.rstrip("\n")
        line = line.rstrip("\r")

        tmp = line.split(",")
        for j in range(nj):
            array[j][nd] = float(tmp[j])
        nd += 1

    for i in range(nd):
        T = array[0][i]
        rho = array[1][i]
        R = array[6][i]
        err = array[7][i]
        if float(R) > 0:
            x.append(T)
            y.append(R)
        if (R < 0):
            FDO.write("###")
        FDO.write("%7.2f %11.4e %11.4e %11.4e\n" %(T, rho, R, err))

    plt.plot(x,y,marker=".")
    #print(min(y))
    if max(y)/min(y) >= 100:
        plt.yscale("log")
    plt.xlabel("T(K)")
    plt.ylabel("R(Ohm)")
    plt.savefig(in_file+".png")
    plt.clf()

FDI.close()
FDO.close()

