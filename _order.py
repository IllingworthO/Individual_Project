import __main as m

def order_menu():
    while True:
                    #  PRINT product menu options
                    m.print_menu("Orders Menu", "Return to Main Menu", "Print Order Dictionary", "Add New Order", "Update Order Status", "Update Order", "Delete Order")
                    
                    #  GET user input for product menu option
                    choice = m.get_input_int(False, 5)

                    #  IF user input is 0:
                    #  RETURN to main menu
                    if choice == 0:
                        print("Returning to Main Menu...")
                        break

                    #  ELSE IF user input is 1:
                    if choice == 1:
                        #  PRINT orders dictionary
                        m.print_list(m.order_list)
                        print(input("Press 'Enter' to continue..."))

                    #  ELSE IF user input is 2:
                    elif choice == 2:
                        #  GET user input for customer name
                        #  APPEND order to orders list
                        while True:
                            m.create_item(m.order_list, m.order_table)

                            print("Would you like to add another?\n0: No\n1: Yes")
                            choice = m.get_input_int()
                            if choice == 0:
                                break

                    #  ELSE IF user input is 3:
                    elif choice == 3:
                        # UPDATE existing order status
                        #  PRINT orders list with its index values
                        m.print_list(m.order_list)
                    
                        #  GET user input for order index value
                        try:
                            order = m.order_list[m.get_input_int('Please input index of order you wish to update...')]
                        except:
                            print('index not found...')

                        #  PRINT order status list with index values
                        m.print_list(m.order_status_list)

                        #  GET user input for order status index value

                        try:
                            status = m.order_status_list[m.get_input_int('Please select which status to update the order with...')]
                        except:
                            print('index not found...')
                        #  UPDATE status for order
                        order.update({"status": status})

                        #update sql log
                        sql = "UPDATE %s SET status = '%s' WHERE id = '%s'" % (m.order_table, status, order['id'])
                        m.sql_log.append(sql)

                    #  ELSE IF user input is 4:
                    elif choice == 4:    
                        #  # STRETCH - UPDATE existing order
                        while True:
                            try:
                                m.update_item(m.order_list, m.order_table)
                                break
                            except:
                                print('Update failed... Please enter valid index...')
                        
                    #  ELSE IF user input is 5:
                    #  # STRETCH GOAL - DELETE order
                    elif choice == 5:
                        #  DELETE order at index in order list
                        m.delete_item(m.order_list, m.order_table)