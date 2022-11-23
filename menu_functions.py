from get_input_functions import *
import __main as m

#print menus
def print_menu(menu, *options):
    count = 0
    print(f"Welcome to the {menu}...")
    print("Please select one of the following:")

    for option in options:    
        print(f"{count}: {option}")
        count += 1

#print each elemment in list with their index
def print_list(obj_list):
    i = 0
    #PRINT product names with its index value
    for x in obj_list:
        print(f"{i}: {x}")
        i += 1
    # header = obj_list[0].keys()
    # rows =  [x.values() for x in obj_list]
    # print(tabulate.tabulate(rows, header))


    

#create dictionary object then append to relevant list
def create_item(obj_list, database_table):
    new_dict = {}
    
    for key in obj_list[0].keys():
        if 'id' in key:
            last_obj = obj_list[-1]

            new_dict.update({key:(int(last_obj[key]))+ 1})
            continue

        print(f'please enter value for {key}...')
        value = get_input_str()

        #key_value_pair = {key:value}
        new_dict.update({key:value})
        
    obj_list.append(new_dict)
    

    rows = ', '.join(f"'{x}'" for x in list(new_dict.values()))
    # for value in new_dict.values():
    #     rows += f"{value},"
    columns = ', '.join(new_dict.keys())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (database_table, columns, rows)
    #     sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (database_table, columns, placeholders)
    m.sql_log.append(sql)

    
    
    
#update specific key in a dictionary object
def update_item(obj_list, database_table):
    print_list(obj_list)

    index = get_input_int('Select item to update...')

    item_update = obj_list[index]
    print(f'You have selected:\n {item_update}')

    

    for key in obj_list[0].keys():
        if 'id' in key:
            id_key = key
            id_value = item_update[key]
            continue

        new_value = get_input_str(f'please enter new value for "{key}"')

        item_update[key] = new_value
        sql = "UPDATE %s SET %s = '%s' WHERE %s = %s" % (database_table, key, new_value, id_key, id_value)
        m.sql_log.append(sql)
    

#Delete dictionary object from list
def delete_item(obj_list, database_table):
    print_list(obj_list)

    index = get_input_int('Select item to Delete...', len(obj_list))

    print(f'You have selcted to delete {obj_list[index]}')

    key_list = list(obj_list[index].keys())
    key = key_list[0]
    value = obj_list[index][key]
    sql = "DELETE FROM %s WHERE %s = %s" % (database_table, key, value)

    m.sql_log.append(sql)

    del obj_list[index]