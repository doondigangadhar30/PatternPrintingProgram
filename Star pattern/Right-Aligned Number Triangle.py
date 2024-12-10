n = int(input("Enter the number of rows: "))
for i in range(n):
    k = n - (i + 1)
    print(" " * k, end=" ") 
    print("*" * (i + 1), end=" ") 
    print()
