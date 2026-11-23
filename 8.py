# Find the sum of natural numbers from 1 to N

n = int(input("n : "))
sum = 0

for i in range(1, n+1, 1):
    sum = sum+i
print("sum : ", sum)    