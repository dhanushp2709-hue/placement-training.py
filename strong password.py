word=input()
length=len(word)
u=0
l=0
n=0
s=0
if length>=8:
    for w in word:
        if w.isupper():
            u=1
        elif w.islower():
            l=1
        elif w.isdigit():
            n=1
        else:
            s=1
if(u+l+n+s==4):
    print("Strong password")
else:
    print("Weak password")
