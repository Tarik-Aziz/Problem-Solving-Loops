# Print the multiplication table of a number

n = int(input("n : "))
mult = 1

for i in range(1, n + 1, 1):
    mult = n * i
    print(n, "*" , i ,"=" , mult)    
    
   