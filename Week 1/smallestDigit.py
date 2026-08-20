num=int(input("enter num:"))
smalest=9
#changed due to edge case (if i enter 0 it is showing 9 is smallest num)

if num == 0:
    smalest=0
else:
    while num>0:
        digit=num%10

        if digit<smalest:
            smalest=digit
        num =num//10

print(smalest)