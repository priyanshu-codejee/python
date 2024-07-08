# Inverted Pyramid of n steps

def inv_pyramid(n):
    for i in range(n):
        print(i*" ",end=' ')
        print((2*(n-i)-1)*"*",end=' ')
        print()
inv_pyramid(6)