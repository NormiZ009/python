no1 = 200
no2 = 100
sum = 0
while no2 <= no1:
    if no2%11==0 and no2%2!=0:
        print(no2)
        sum = sum + no2
    no2 = no2 + 1
print(f"total is {sum}")