input = "input.csv"
FDI = open(input,'r')

for line in FDI:
    k=0
    line = line.rstrip('\n')
    line = line.rstrip('\r')

    tmp = line.split(",")
    i = int(tmp[0])
    i2= float(tmp[1])
    i3= float(tmp[2])

    if ((i%2)!=0):
        k+=i2+i3
        print("%d行目: 2列目+3列目: %6.2f" % (i,k))
    else:
        print("%d行目:     4列目: %6s" % (i,tmp[3]))
FDI.close()