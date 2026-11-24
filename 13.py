# Calculate cubes of numbers from 1 to N

n = int(input("n : "))
for i in range (1, n + 1, 1):
    cube = i * i * i
    print(i, "*", i, "*", i, "=", cube)