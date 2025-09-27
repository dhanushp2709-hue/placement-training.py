n=int(input())
a=input()
l=len(a)
ans = n%l
print(a[ans:l]+a[0:ans])
