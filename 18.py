# Find the first and last digit

digit = int(input("digit = "))

last_digit = digit % 10

while digit > 9:
      digit = digit // 10

print("First digit : ", digit, "\n","Last digit : ",last_digit)



    