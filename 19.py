# Find the sum of first and last digit

num = int(input("num : "))

last_digit = num % 10

while num >= 10:
    num = num // 10

print("the sum of first and last digit = ", num + last_digit)    



