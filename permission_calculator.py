# author: morteza abdollahi
# title: permission offline calcaulator
# description: simple a free permission calculator
# language programming: python 3.x
# this is script for convert permission linux file
    

# split a string every 3 chars
    # example: 'aaabbbccc' is iterable and returning ['aaa', 'bbb', 'ccc']
def split_string_every_3_chars(iterable):
    split_number = 3
    every_3_chars = ''; result = []
    for item in iterable:
        every_3_chars += item
        if len(every_3_chars) == split_number:
            result.append(every_3_chars)
            every_3_chars = ''
    return result

def type_permission(permission):
    if permission[0] == '-':
        return 'file'
    elif permission[0] == 'd':
        return 'directory'
    return ''

# compute sum of digits of a given string
def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())

# permission string to octal
    # returning number permission
    # exmaple: permission is 'rwxr-xr-x' and convert to \? yes is permission number 
    # formula 421 401 401 => 4+2+1  4+0+1  4+0+1  =? 755 and 755 is octal
def permission_string_to_octal(string_permission):
    global number_permission
    result = ''
    dictate = {'r': 4, 'w': 2, 'x': 1}  # r -> Read & w -> Write & x -> Execute
    if type_permission(string_permission):
        string_permission = string_permission[1:]
    number_permission = ''
    for char in string_permission:
        number_permission += str(dictate[char]) if char != '-' else '0'
    # getting octal number
    for number in split_string_every_3_chars(number_permission):
        result += str(sum_digits(number))
    return result

# octal to permission string
def octal_to_permission_string(octal):
    result = ''
    dictate = {'r': 4, 'w': 2, 'x': 1}  # r -> Read & w -> Write & x -> Execute
    # Iterare over each of the digits octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions valus
        for letter, value in dictate.items():
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += '-'
    return result

# show groups of permission
def get_groups_number_permission(string_permission):
    #         Owner  Group  Others
    # Read      4      4      4
    # Write     2      0      0
    # Execute   1      1      1
    # ----------------------------
    # Totals    7      5      5
    index = 0
    groups = {'Owner': '', 'Group': '', 'Others': ''}
    if type_permission(string_permission):
        string_permission = string_permission[1:]
    for section_number in split_string_every_3_chars(number_permission):
        groups[list(groups)[index]] = section_number.replace('0', '-')
        index += 1
    return groups 

# chekcing id valid permission for calculate
def is_valid(string_permission):
    if len(string_permission) > 10 and len(string_permission) <= 0:
        return False
    return True

# main function
def main():
    option_text = """option:
        select 1> convert octal to permission string,
        select 2> convert permission string to octal,
        select 3> help,
        select 4> exit!"""
    print (option_text)
    while True:
        selected = input("?>> ")
        if selected == "1":
            octal = int(input('please enter octal: '))
            print (octal_to_permission_string(octal))
        elif selected == "2":
            string_permission = input('please enter your unix permission for calculate: ')
            if is_valid(string_permission):
                print (type_permission(string_permission) + ' ' + permission_string_to_octal(string_permission))
                print (get_groups_number_permission(string_permission))
            else:
                print ('invalid')
        elif selected == "3":
            print (option_text)
        elif selected == "4":
            print ('exit from project !!')
            exit()
        else:
            print ("selected error please agin!")
        
if __name__ == '__main__':
    print ('starting project ...')
    main()

#print ('groups : {0}'.format(groups))
#print ('string permission : {0}'.format(string_permission))
#print ('number permission : {0}'.format(number_permission))
#print ('result : {0}'.format(absolute_notation_octal))
