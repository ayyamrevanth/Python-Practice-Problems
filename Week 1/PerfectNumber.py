num=int(input("enter a number:"))
total=0

if num<=0:
    print("enter a positive integer")
else:
    for i in range(1,num):
        if num%i==0:
            total+=i
    if num==total:
            print(f"{num} is a Perfect Number")
    else:
        print(f"{num} is not a Perfect Number")