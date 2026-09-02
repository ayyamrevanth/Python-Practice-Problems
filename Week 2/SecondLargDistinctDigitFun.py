def sec_larg(n):
    larg=-1
    s_larg=-1
    if n==0:
        return None
    else:
        while n>0:
            digit=n%10
            if digit>larg:
                s_larg=larg
                larg=digit
            elif digit>s_larg and digit!=larg:
                s_larg=digit
            n//=10
    if s_larg==-1:
        return None
    return s_larg
print(sec_larg(int(input("enter:"))))