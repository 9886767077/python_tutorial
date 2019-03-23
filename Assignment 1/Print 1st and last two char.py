string=input("Enter string:")
count=0
for i in string:
      count=count+1
newstring=string[0:2]+string[count-2:count]

print(newstring)

