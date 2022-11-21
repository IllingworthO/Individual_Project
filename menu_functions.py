from get_input_functions import *

#print menus
def print_menu(menu, *options):
    count = 0
    print(f"Welcome to the {menu}...")
    print("Please select one of the following:")

    for option in options:    
        print(f"{count}: {option}")
        count += 1

#print each elemment in list with their index
def print_list(list):
    i = 0
    #PRINT product names with its index value
    for x in list:
        print(f"{i}: {list[i]}")
        i += 1

#create dictionary object then append to relevant list
def create_item(list):
    new_dict = {}

    for key in list[0].keys():
        print(f'please enter value for {key}...')
        value = get_input_str()

        #key_value_pair = {key:value}

        new_dict.update({key:value})

    list.append(new_dict)

#update specific key in a dictionary object
def update_item(list):
    print_list(list)

    index = get_input_int('Select item to update...', list.len())

    item_update = list[index]
    print(f'You have selected:\n {item_update}')

    for key in list[0].keys():
        new_value = get_input_str(f'please enter new value for "{key}"')

        item_update[key] = new_value

#Delete dictionary object from list
def delete_item(list):
    print_list(list)

    index = get_input_int('Select item to Delete...', len(list))

    print(f'You have selcted to delete {list[index]}')
    del list[index]