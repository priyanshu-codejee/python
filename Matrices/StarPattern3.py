# Upper left Triangle of n steps

def upper_left_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print("#",end=' ')
        print()    
upper_left_triangle(7)