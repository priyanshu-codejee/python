# Pascal Triangle

def num_pyramid(n):
    mylist1 = [1,1]
    print((n-1)*" ",end=' ')
    print(1,end=' ')
    print()
    print((n-2)*" ",end=' ')
    print(1,end=' ')
    print(1,end=' ')
    print()
    for i in range(3,n+1):
        mylist2 = []
        print((n-i)*" ",end=' ')
        print(1,end=' ')
        mylist2.append(1)
        for j in range(i-2):
            num = mylist1[j] + mylist1[j+1]
            mylist2.append(num)
            print(num,end=' ')
        print(1,end=' ')
        print()
        mylist2.append(1)           
        mylist1 = mylist2

num_pyramid(5)