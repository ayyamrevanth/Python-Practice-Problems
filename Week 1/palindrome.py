num=int(input("enter num:"))
reverse =0
original = num  # updated after understanding error

while num>0:
    digit=num%10 # gets the last digit as reminder
    reverse=reverse*10+digit
    num=num//10  # deletes the last digit
print(f"reversed num is {reverse}")

if reverse == original:
    print(f"The given {original} is palindrome")
else:
    print(f"The given {original} is not a palindrome")