num=int(input("enter num:"))
even_digits=0
odd_digits=0

if num==0:                  #changed due to 0 input edge case
    even_digits=1
else:
    while num>0:
        digit=num%10

        if digit%2==0:
            even_digits+=1
        else:
            odd_digits+=1
        num=num//10
print("Even digits:",even_digits)
print("Odd digits:",odd_digits)