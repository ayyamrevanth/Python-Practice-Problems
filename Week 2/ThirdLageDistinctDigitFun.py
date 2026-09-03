def thirdLargest(m):
    larg=-1
    se_larg=-1
    thir_larg=-1
    if m==0:
        return None
    else:
        while m>0:
            digit=m%10
            if digit>larg:
                thir_larg=se_larg
                se_larg=larg
                larg=digit
            elif digit>se_larg and digit !=larg:
                thir_larg=se_larg
                se_larg=digit
            elif digit>thir_larg and digit != se_larg and digit != larg:
                thir_larg=digit
            m//=10

    if thir_larg==-1:
        return None
    return thir_larg
print(thirdLargest(int(input("enter num:"))))