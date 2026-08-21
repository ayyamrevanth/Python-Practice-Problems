num=int(input("enter num:"))


if num==0:
    print(0)
else:
    for i in range(1,num+1):
        if num%i==0:
            print(i)
