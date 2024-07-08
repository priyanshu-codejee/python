# Diamond

def diamond(n):
    for i in range(n):
        print((n-1-i)*" ",end=' ')
        print((2*i+1)*"*",end=' ')
        print()
    for i in range(1,n):
        print(i*" ",end=' ')
        print((2*(n-i)-1)*"*",end=' ')
        print()
diamond(5)
