#Method 1
def check_pallindrome(mystring):
    for i in range(len(mystring)//2+1):
        if (mystring.lower())[i] != (mystring.lower())[-1-i]:
            break
    if i == len(mystring)//2:
        print("Yes, a pallindrome")
    else:
        print("not pallindrome")    
check_pallindrome("100001")

#Method 2

def reverse(mystring):
    return(mystring[::-1])

def check_pallin(mystring):
    return (reverse(mystring)==mystring)

print(check_pallin("abcba"))