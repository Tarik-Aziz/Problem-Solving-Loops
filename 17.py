# Count the number of digits in an integer

digit = int(input("digit : "))
count = 0

while digit > 0:
    digit = digit // 10
    count += 1

print(count)    
    
