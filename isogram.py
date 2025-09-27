text=input().lower()
letters=set()
is_isogram=True
for char in text:
    if char.isalpha():
        if char in letters:
            is_isogram=False
            break
        letters.add(char)
if is_isogram:
    print("ISOGRAM")
else:
    print("NOT ISOGRAM")
