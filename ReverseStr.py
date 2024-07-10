def reverse(mystring):
    newstring = ""
    for i in mystring:
        newstring = i + newstring
    print(newstring)    
reverse("Hello")