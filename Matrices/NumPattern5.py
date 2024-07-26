# Spiral Matrix

def spiral(x):
    mylist = []
    count = 0
    n=x
    for i in range(x):
            mylist.append([])
    for j in range((n+1)//2):
        for i in range(n):
            count += 1
            mylist[j].append(count)
        for i in range(n-1):
            count += 1
            mylist[j+i+1].append(count)
        for i in range(n-1):
            count += 1
            mylist[n-1].append(count)
        for i in range(n-1,0,-1):
            count += 1
            mylist[i].append(count)

        n = n-2
    return mylist

        
        


        
print(spiral(5))
