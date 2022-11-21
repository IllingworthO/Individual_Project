from __Main__ import *

def save_menu():
    choice = get_input_int('Do you wish to save?\n0: Exit without saving\n1: Save to database\n2: Save to csv(local)')

    if choice == 0:
        return
    
    if choice == 1:
        while True:
            table_to_save = get_input_int('Which database would you like to save to?\n0:Return\n1: Products\n2: Couriers\n3: Orders\n4:Save All', 4)

            if table_to_save == 0:
                break
            elif table_to_save == 1:
                export_to_database('products', product_list)
            elif table_to_save == 2:
                export_to_database('couriers', courier_list)
            elif table_to_save == 3:
                export_to_database('orders', order_list)
            elif table_to_save == 4:
                export_to_database('products', product_list)
                export_to_database('couriers', courier_list)
                export_to_database('orders', order_list)
            else:
                print('Invalid input...')

    if choice == 2:
        while True:
            list_to_save = get_input_int('which list would you like to save?\n0:Return\n1: Products\n2: Couriers\n3: Orders\n4:Save All', 4)
            
            if list_to_save == 0:
                break
            if list_to_save == 1:
                write_list('product list', product_list, product_csv_path)
            if list_to_save == 2:
                write_list('courier listt', courier_list, courier_csv_path)
            if list_to_save == 3:
                write_list('order list', order_list, orders_csv_path)
            if list_to_save == 4:
                write_list('product list', product_list, product_csv_path)
                write_list('courier lsit', courier_list, courier_csv_path)
                write_list('order list', order_list, orders_csv_path)