def smallest_multiple(n):
    numlist = list(range(1,n+1))
        for i in range(n*(n-1),n**n):
            for j in numlist:
                if i%j != 0:
                    break
            if j==n:
                print(i)

smallest_multiple(10)
