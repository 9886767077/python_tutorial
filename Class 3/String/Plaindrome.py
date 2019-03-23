mystring= input("please enter the string")

reverse= mystring[-1::-1]

print("origional string is {}, and reverse string is {}".format(mystring,reverse))

if mystring == reverse:
    print("its a palindrome:")
else:
    print("sorry its not a palindrome:")
