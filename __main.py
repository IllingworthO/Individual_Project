#Imports
from _courier import *
from csv_functions import *
from database_functions import *
from get_input_functions import *
from menu_functions import *
from _order import *
from _product import *
from _save import *

#Global Variables
product_csv_path = 'csv_files\products.csv'
product_table = 'products'
product_list = import_database(product_table)

courier_csv_path = 'csv_files\couriers.csv'
courier_table = 'couriers'
courier_list = import_database(courier_table)

orders_csv_path = 'csv_files\orders.csv'
order_table = 'orders'
order_status_list = ["Preparing", "Awaiting Pickup", "Out for Delivery", "Delivered"]
order_list = import_database(order_table)

#list of sql statement strings.
sql_log = []

def main():
    while True:
        # PRINT main menu options
        print_menu("Main Menu", "Exit", "Products Menu", "Couriers Menu", "Orders Menu")
        
        # GET user input for main menu option
        choice = get_input_int()

        # IF user input is 0:
        #  EXIT app
        if choice == 0:
            export_to_database(m.sql_log)

            print("Closing Programme...")
            break

        # # products menu
        # ELSE IF user input is 1:
        elif choice == 1:
            product_menu()


        # # Couriers menu
        # ELSE IF user input is 2:
        elif choice == 2:
            courier_menu()
                
        # # orders menu
        # ELSE IF user input is 3:
        elif choice == 3:
            order_menu()
        
        # #save menu
        # elif choice == 4:
        #     for x in sql_log:
        #         print(x)
        #     save_menu()


if __name__ == '__main__':
    main()