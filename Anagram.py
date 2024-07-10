def create_dic(mystring):
    dic = {}
    for i in mystring:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

