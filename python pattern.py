n= int(input())
if(n % 2==0):
    center_row1 = [n//2-1,n//2]
    center_col1 = [n//2-1,n//2]
else:
    center_row1=[n//2]
    center_col1=[n//2]
for i in range(n):      
    for j in range(n):    
        if(i in center_row1 and j in center_col1):
            print("0", end="")  
        else:
            print("1", end="")  
    print()  
