def capitalise(mystring):
    newstring = mystring[0].capitalize()
    for i in range(1,len(mystring)):
        if mystring[i-1] == ' ':
            newstring = newstring + mystring[i].capitalize()
        else:
            newstring = newstring + mystring[i]
    return newstring
print(capitalise("a lazy fox"))    
