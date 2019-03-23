para = input("Enter a string :")

mystring = ""
for c in para:
    if c in mystring:
        print("Current val {}".format(mystring))
        print("Repeted {}".format(c))
    else:
        mystring = mystring + c

