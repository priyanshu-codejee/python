# nxn Number Matrix 

def matrix(n):
    for i in range(n):
        num = 5*(i+1)
        for j in range(n):
            print(num,end=' ')
            num-=1
        print()
matrix(5)            