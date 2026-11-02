text="Sys""te@234m"
vowels,consonants,digits,spaces=0,0,0,0
for ch in text:
    if ch in "AEIOUaeiou":
        vowels+=1

    elif ch.isalpha():
        consonants+=1

    elif ch.isdigit():
        digits+=1

    else:
        spaces+=1
    
print("vowels count is: ",vowels)
print("consonants count is: ",consonants)
print("digits count is : ",digits)
print("spaces count is: ",vowels)
