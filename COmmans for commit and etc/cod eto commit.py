n = int(input("enter a number: "))

i = 0
output_string = "number divisible by 5 between 0 to {} are : ".format(n)

while (i<=n):
    if(i%5==0):
        # print(i)
        if(i==n):
            output_string = output_string + str(i)
        else:
            output_string = output_string + str(i) + ","
    i = i+1

print(output_string)



