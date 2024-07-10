import math
#Method 1
def reverse(mystring):
    return(mystring[::-1])

def reverse_int(n):
    if n>0:
        print(int(reverse(str(n))))
    else:
        print((-1)*int(reverse(str(-n))))
reverse_int(900)


#Method 2
def rev_int(n):
    num = 0
    if n>0:
        x=n
        sign = 1
    else:
        x=-n  
        sign = -1  
    while x>0:
        num = num + (x%10)*(10**int(math.log(x,10)))
        x=x//10
    print(num*sign)
rev_int(-1204)


#Method 3
def rev_num(n):
    rev = 0
    if n>0:
        x=n
        sign = 1
    else:
        x=-n  
        sign = -1 
    while x>0:
        rev = rev*10 + x%10
        x=x//10
    print(rev*sign)        
rev_num(-245)