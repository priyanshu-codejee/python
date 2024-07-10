# Method 1
def max_char(mystring):
    max_char = ""
    max_count = 0
    for i in mystring:
        count = 0    
        for j in mystring:
            if j==i:
                count += 1
        if count>max_count:
            max_count=count
            max_char=i       
    print(max_char,max_count)
max_char("aaaabbccccc")


# Method 2

def create_dic(mystring):
    dic = {}
    for i in mystring:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
print(create_dic("aaabbcccccddddddd"))

def maximum_char(dic):
    max_count = 0
    for i in dic:
        if dic[i]>max_count:
            max_count=dic[i]
            max_char=i
    return(max_char,max_count)      
print(maximum_char(create_dic("aaabbcccccddddddd")))
