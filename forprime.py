flag = 0
num = int(input("enter number: "))
for i in range(1,num+1):
    if num%i==0:
        flag = flag + 1
    pass
if(flag==2):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")