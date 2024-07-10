#Method 1
def subarray(array,chunksize):
    chunk = []
    mylist = []
    for i in array:
        if len(chunk) == chunksize:
            mylist.append(chunk)
            chunk = []     
        chunk.append(i)
    if len(chunk)<chunksize:
        mylist.append(chunk)    
    return(mylist)        
print(subarray([1,2,3,4,5,6,7],3))


#Methohd2
def sub_array(array,chunksize):
    i=0
    mylist=[]
    while i<len(array):
        mylist.append(array[i:i+chunksize])
        i=i+chunksize
    return(mylist)
print(sub_array([1,2,3,4,5,6,7],3))

        