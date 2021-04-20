a = 1
b = [1, "test"]
b[0] = 2

print("a = ",a)
print("b = ",b)
print("b[0], b[1] = ",b[0], b[1])

#b[2] = 6
b.append(5.80)

print("b[0]=%5d, b[1]=%5s, b[2]=%5.2f" %(b[0], b[1], b[2]))

b[0] = "a"
print("b[0]=%5s" %(b[0]))
#print("b[0] = %5d" %(b[0]))
