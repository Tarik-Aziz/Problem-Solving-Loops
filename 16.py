# Filter numbers using break and continue

n = [1,2,3,4,5,6,7,8,9,10]

i  = 0
while i < len(n):
    num = n[i]
    i += 1
    if num % 2 == 0:
        continue
    if num == 9:
        break
    print(num)
    