a=int(input("enter num:"))
larg=-1                      #we are using -1 beacuse 
sec_l=-1                     #if input is 10 second larg is 0,it will give incorrect answer

while a>0:
    digit=a%10
    if digit>larg:
        sec_l=larg
        larg=digit
    
    elif digit>sec_l and digit != larg:
        sec_l=digit
    a=a//10
if sec_l==-1:                                    
    print("No second largest digit")
else:
    print("Second largest digit is:",sec_l)