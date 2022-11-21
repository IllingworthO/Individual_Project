from __Main__ import *

def order_menu():
    while True:
                    #  PRINT product menu options
                    print_menu("Orders Menu", "Return to Main Menu", "Print Order Dictionary", "Add New Order", "Update Order Status", "Update Order", "Delete Order")
                    
                    #  GET user input for product menu option
                    choice = get_input_int(False, 5)

                    #  IF user input is 0:
                    #  RETURN to main menu
                    if choice == 0:
                        print("Returning to Main Menu...")
                        break

                    #  ELSE IF user input is 1:
                    if choice == 1:
                        #  PRINT orders dictionary
                        print_list(order_list)

                    #  ELSE IF user input is 2:
                    elif choice == 2:
                        #  GET user input for customer name
                        #  APPEND order to orders list
                        while True:
                            create_item(order_list)

                            print("Would you like to add another?\n0: No\n1: Yes")
                            choice = get_input_int()
                            if choice == 0:
                                break

                    #  ELSE IF user input is 3:
                    elif choice == 3:
                        # UPDATE existing order status
                        #  PRINT orders list with its index values
                        print_list(order_list)
                    
                        #  GET user input for order index value
                        print('Please input index of order you wish to update...')
                        try:
                            order = order_list[get_input_int()]
                        except:
                            print('index not found...')
                        #  PRINT order status list with index values
                        print_list(order_status_list)
                        #  GET user input for order status index value
                        print('Please select which status to update the order with...')
                        try:
                            status = order_status_list[get_input_int()]
                        except:
                            print('index not found...')
                        #  UPDATE status for order
                        order.update({"status": status})

                    #  ELSE IF user input is 4:
                    elif choice == 4:    
                        #  # STRETCH - UPDATE existing order
                        while True:
                            try:
                                update_item(order_list)
                                break
                            except:
                                print('Update failed... Please enter valid index...')
                        
                    #  ELSE IF user input is 5:
                    #  # STRETCH GOAL - DELETE order
                    elif choice == 5:
                        #  DELETE order at index in order list
                        delete_item(order_list)