a=int(input("enter a:"))
b=int(input("enter b:"))
largest=0

for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        if i >largest:
            largest=i
print(largest)