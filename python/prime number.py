num=int(input("enter the number"))
found=0
for i in range(2,num):
    if num%i==0:
        found+=1
        break

if found==0:
    print("prime number")
else:
    print("not a prime number")
