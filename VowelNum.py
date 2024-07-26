def num_of_vowel(mystring):
    dic = {'a':0,'e':0,'i':0,'o':0,'u':0}
    num = 0
    for i in mystring:
        if i in dic:
            num = num + 1
    return [dic,num]
print(num_of_vowel('Why do you ask?'))

