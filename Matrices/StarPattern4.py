# * Pyramid of n steps

def pyramid(n):
    for i in range(n):
        print((n-1-i)*" ",end=' ')
        print((2*i+1)*"*",end=' ')
        print()
pyramid(5)