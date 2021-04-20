b = [1, "test", 5.80]

for i in range(3):
    for k in range(0, i+1):
        print("b[%d]=" %(k),end="")
        print("%5s" %(str(b[k])), end="")
    print("")
