# NUmber Pyramid of N steps

def pyramid(n):
    for i in range(n):
        print((n-1-i)*" ",end=' ')
        str1 = ""
        str2 = ""
        num=1
        for j in range(i+1):
            str1 = str1 + str(num)
            num += 1
        num=i    
        for k in range(i):
            str2 = str2 + str(num)
            num -= 1    
        print(str1+str2,end=' ')
        print()
pyramid(5)        