def upper_left_triangle(n):
    for i in range(n):
        for j in range(n-1-i):
            print("#",end=' ')
        print()    
upper_left_triangle(5)