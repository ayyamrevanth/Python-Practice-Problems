num=int(input("enter num:"))
total=0

if num<=0:
    print("enter integer")
else:
    for i in range(1,num+1):
        if num%i==0:
            total+=i
    print(total)