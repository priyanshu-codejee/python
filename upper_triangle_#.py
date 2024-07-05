def lower_right_triangle(n):
    for i in range(n):
        for j in range(n-1-i):
            print("#",end=' ')
        print()    
lower_right_triangle(5)

