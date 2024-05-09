num = int(input("enter number: "))
flag = 0
i = num
while i >= 1:
    if num%i==0:
        flag = flag + 1
    i = i - 1
if(flag == 2):
    print("number is prime")
else:
    print("number is not prime")