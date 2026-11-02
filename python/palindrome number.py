p=242
sum=0
temp=p
while p>0:
    q=p%10
    sum=sum*10+q
    p//=10
if sum==temp:
    print("Palindrome number ")

else:
    print("Not a Palindrome number")
