n = int(input("Enter the number of rows: "))
for i in range(n):
    k=n-(i+1)
    print(" "*k,end=" ")
    j=(2*i)+1
    print("*"*j,end="")
    print()
for i in range(1,n):
    print(" "*i,end=" ")
    k=2*(n-i-1)+1
    print("*"*k,end=" ")
    print()
