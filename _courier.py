import __main as m

def courier_menu():
    while True:
                    #  PRINT couriers menu options
                    m.print_menu("Couriers Menu", "Return to Main Menu", "Print Couriers List", "Add New Couriers", "Update Courier", "Delete courier")
                    
                    #  GET user input for courier menu option
                    choice = m.get_input_int(False, 4)

                    #  IF user inputs 0:
                    #  RETURN to main menu
                    if choice == 0:
                        print("Returning to Main Menu...")
                        break
                    
                    #  ELSE IF user input is 1:
                    #  PRINT couriers list
                    elif choice == 1:
                        print("Printing courier List...")
                        m.print_list(m.courier_list)
                        print(input("Press 'Enter' to continue..."))

                    #  ELSE IF user input is 2:
                    # CREATE new courier
                    elif choice == 2:
                        while True:
                            m.create_item(m.courier_list, m.courier_table)

                            print("Would you like to add another?\n0: No\n1: Yes")
                            choice = m.get_input_int()
                            if choice == 0:
                                break
                        
                        
                    #  ELSE IF user input is 3:
                    #STRETCH GOAL - UPDATE existing courier
                    elif choice == 3:
                        while True:
                            try:
                                m.update_item(m.courier_list, m.courier_table)
                                break
                            except:
                                print('Update failed... Please enter valid index...')

                    #  ELSE IF user input is 4:
                    #  # STRETCH GOAL - DELETE courier
                    if choice == 4:
                        m.delete_item(m.courier_list, m.courier_table)