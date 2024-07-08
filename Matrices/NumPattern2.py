# Lower Left Triangle of n steps

def lower_left_triangle(n):
    num=1
    for i in range(n):
        for j in range(i+1):
            print(num,end=' ')
            num += 1
        print()            
lower_left_triangle(5)            

