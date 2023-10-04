
string = input('Введите строку для того чтобы её преобразовать в новую').split(' ')

def remove_Spaces(string):
    new_string =''
    for i in string:
            new_string += i

    return new_string

def remove_repeating_symbols(string):
    temp_list= []
    new_string = ''

    for i in string:
        if i not in temp_list:
            temp_list.append(i)

    for j in range(0, len(temp_list)):
        new_string += temp_list[j]

    return new_string


no_spaces = remove_Spaces(string)

print(remove_repeating_symbols(no_spaces))




