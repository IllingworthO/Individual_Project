import __main as m

def product_menu():
    while True:
                #  PRINT product menu options
                m.print_menu("Products Menu", "Return to Main Menu", "Print Products List", "Add New Product", "Update Product", "Delete Product")
                
                #  GET user input for product menu option
                choice = m.get_input_int(False, 4)

                #  IF user inputs 0:
                #  RETURN to main menu
                if choice == 0:
                    print("Returning to Main Menu...")
                    return
                
                #  ELSE IF user input is 1:
                #  PRINT products list
                elif choice == 1:
                    print("Printing Product List...")
                    m.print_list(m.product_list)
                    print(input("Press 'Enter' to continue..."))

                #  ELSE IF user input is 2:
                # CREATE new product
                elif choice == 2:
                    while True:
                        m.create_item(m.product_list, m.product_table)

                        print("Would you like to add another?\n0: No\n1: Yes")
                        choice = m.get_input_int()
                        if choice == 0:
                            break
                    
                #  ELSE IF user input is 3:
                #STRETCH GOAL - UPDATE existing product
                elif choice == 3:               
                    while True:
                            m.update_item(m.product_list, m.product_table)
                            break
                        

                            
                #  ELSE IF user input is 4:
                #  # STRETCH GOAL - DELETE product
                if choice == 4:
                    m.delete_item(m.product_list, m.product_table)