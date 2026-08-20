num=int(input("enter num:"))
reverse = 0
#print(num[::-1])   (not aplicable for interer)
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

print(reverse)