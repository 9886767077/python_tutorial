def odd_values_string(str):
    str = input('enter a string:')
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
            return result

print(odd_values_string)