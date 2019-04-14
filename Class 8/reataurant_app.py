dish1= [1, "noodles", ["noodles", "egg", "salt", "chillisauce"], 250.52, "S", "Veg"]
dish2= [2, "chickennoodles", ["chickennoodles", "egg", "salt", "chillisauce"], 350.52, "M", "Veg"]
dish3= [3, "vegrice", ["vegetables", "onion", "salt", "chillisauce"], 450.52, "S", "Veg"]

menu = [dish1, dish2, dish3]

count = 0
for dish in menu:
    food = dish[4]
    if "S" in food:
        count = count+1
        print("option {}: starter name is {}, price is {}".format(count,dish[1],dish[3]))

