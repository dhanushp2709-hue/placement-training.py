n=int(input())
size=2*n-1
for row in range(size):
    for col in range(size):
        if(row+col==size-1 or row==col):
            print("*",end="")
        else:
            print(" ",end="")
    print()
