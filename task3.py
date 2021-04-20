input = "data1.csv"
line_count = 0
FD = open(input, "r")
loutput = [3, 8, 10]

for line in FD:
    line_count += 1
    line = line.rstrip("\n")
    line = line.rstrip("\r")
    
    tmp = line.split(",")
    if line_count in loutput:
        print("%6s, %6s\n" %(tmp[0], tmp[1]))

FD.close()
