from __Main__ import *

def courier_menu():
    while True:
                    #  PRINT couriers menu options
                    print_menu("Couriers Menu", "Return to Main Menu", "Print Couriers List", "Add New Couriers", "Update Courier", "Delete courier")
                    
                    #  GET user input for courier menu option
                    choice = get_input_int(False, 4)

                    #  IF user inputs 0:
                    #  RETURN to main menu
                    if choice == 0:
                        print("Returning to Main Menu...")
                        break
                    
                    #  ELSE IF user input is 1:
                    #  PRINT couriers list
                    elif choice == 1:
                        print("Printing courier List...")
                        print_list(courier_list)
                        print(input("Press 'Enter' to continue..."))

                    #  ELSE IF user input is 2:
                    # CREATE new courier
                    elif choice == 2:
                        while True:
                            create_item(courier_list)

                            print("Would you like to add another?\n0: No\n1: Yes")
                            choice = get_input_int()
                            if choice == 0:
                                break
                        
                        
                    #  ELSE IF user input is 3:
                    #STRETCH GOAL - UPDATE existing courier
                    elif choice == 3:
                        while True:
                            try:
                                update_item(courier_list)
                                break
                            except:
                                print('Update failed... Please enter valid index...')

                    #  ELSE IF user input is 4:
                    #  # STRETCH GOAL - DELETE courier
                    if choice == 4:
                        delete_item(courier_list)