a=input().strip()
b=input().strip()
if sorted(a)==sorted(b):
    print(a,"and",b,"are Anagrams.")
else:
    print(a,"and",b,"are Not Anagrams.")
