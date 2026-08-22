#Count digits greater than 5
a=int(input("enter num:"))
count=0

while a>0:            
    digits=a%10       #Gives the last digit as reminder       
    if digits>5:
        count+=1
    a=a//10         #it delets last digit

print(count)