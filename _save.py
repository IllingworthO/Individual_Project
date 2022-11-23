import __main as m

def save_menu():
    choice = m.get_input_int('Do you wish to save?\n0: Exit without saving\n1: Save to database\n2: Save to csv(local)')

    if choice == 0:
        return
    
    if choice == 1:
        while True:
            table_to_save = m.get_input_int('Which database would you like to save to?\n0:Return\n1: Products\n2: Couriers\n3: Orders\n4:Save All', 4)

            if table_to_save == 0:
                break
            elif table_to_save == 1:
                m.export_to_database('products', m.sql_log)
            elif table_to_save == 2:
                m.export_to_database('couriers', m.sql_log)
            elif table_to_save == 3:
                m.export_to_database('orders', m.sql_log)
            elif table_to_save == 4:
                m.export_to_database('products', m.sql_log)
                m.export_to_database('couriers', m.sql_log)
                m.export_to_database('orders', m.sql_log)
            else:
                print('Invalid input...')

    if choice == 2:
        while True:
            list_to_save = m.get_input_int('which list would you like to save?\n0:Return\n1: Products\n2: Couriers\n3: Orders\n4:Save All', 4)
            
            if list_to_save == 0:
                break
            if list_to_save == 1:
                m.write_list('product list', m.roduct_list, m.product_csv_path)
            if list_to_save == 2:
                m.write_list('courier listt', m.courier_list, m.courier_csv_path)
            if list_to_save == 3:
                m.write_list('order list', m.order_list, m.orders_csv_path)
            if list_to_save == 4:
                m.write_list('product list', m.product_list, m.product_csv_path)
                m.write_list('courier lsit', m.courier_list, m.courier_csv_path)
                m.write_list('order list', m.order_list, m.orders_csv_path)