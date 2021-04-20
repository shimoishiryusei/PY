b = [1, "test", 5.80, 4]

for i in range(0,4):
    if (i == 3):
        continue
    elif (i % 2 == 0):
        print("b[%d]=%5.2f" %(i, b[i]))
    else:
        print("b[%d]=%5s" %(i, b[i]))

