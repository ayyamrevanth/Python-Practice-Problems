num=int(input("enter num to check prime or not:"))
is_prime=True

if num<=1:
    is_prime=False
else:
    for i in range(2,num):           #for i in range(2, int(num ** 0.5) + 1): (for large nums)
        if num%i==0:
            is_prime = False
                                     # add break


if is_prime:
    print(f"{num} is prime number")
else:
     print(f"{num} is not prime number")
    



"""if num%i==0:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not a prime number")"""