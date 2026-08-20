a = int(input("enter a value:"))
b = int(input("enter b value:"))

ope =input("enter:")

if ope == "+":
    print(a+b)
elif ope == "-":
    print(a-b)
elif ope == "*":
    print(a*b)
elif ope == "/": #correction
    if b==0:
        print("cannot divided by zero")
    else:
        print(a/b)
elif ope == "%":
    if b==0:
        print("cannot divided by zero")
    else:
        print(a/b)
else:
    print("enter a valid operator")