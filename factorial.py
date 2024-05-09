#when factorial need to find the formula is fact = fact * i,where val of fact is 1
#when finding the sum of number,the formula is sum = sum + i,where val of sum is 0
i = int(input("enter the number: "))
fact = 1
while i > 0:
    fact = fact * i
    print(fact)
    i = i - 1