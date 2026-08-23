def isPrime(n):
    prime=True
    if n<=1:
        prime=False
    else:
        for i in range(2,n):
            if n%i==0:
                return False

    return prime
print(isPrime(int(input("Enter num:"))))