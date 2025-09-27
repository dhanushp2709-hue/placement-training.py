n=input()
count=0
for ch in n:
    if ch=='(':
        count+=1
    elif ch==')':
        count-=1
    if count<0:
        break
if count==0:
    print("Balanced")
else:
    print("Unbalanced")
