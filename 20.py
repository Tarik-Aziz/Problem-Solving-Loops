# 20 Swap the first and last digit

num = input("num : ")

digit = list(num)

temp = digit[0]
digit[0] = digit[-1]
digit[-1] = temp

print("".join(digit))