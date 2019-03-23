string = input("Enter any string to remove all spaces: ");
if string == 'x':
    exit();
else:
    new_string = string.replace(" ","");
    print("\nNew string after eleminating all spaces:");
    print(new_string);