#x = input("enter num between 1500 to 2700")
R = {}
for x in range (1500,2700):
        if (x%7==0) and (x%5==0):
            R.append(string(x))
            print (','.join(R))