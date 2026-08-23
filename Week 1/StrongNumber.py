n=int(input("enter num:"))
org=n
total=0

if n<=0:
    print(f"{org} is not strong number")
else:
    while n>0:
        digit=n%10
        fact=1        #We are using local var,Every digit needs its own fresh factorial calculation.
        for i in range(1,digit+1):
            fact*=i
        total+=fact
        n=n//10
    if org==total:
        print(f"{org} is strong number")
    else:
        print(f"{org} is not strong number")