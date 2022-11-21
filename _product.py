from __Main__ import *

def product_menu():
    while True:
                #  PRINT product menu options
                print_menu("Products Menu", "Return to Main Menu", "Print Products List", "Add New Product", "Update Product", "Delete Product")
                
                #  GET user input for product menu option
                choice = get_input_int(False, 4)

                #  IF user inputs 0:
                #  RETURN to main menu
                if choice == 0:
                    print("Returning to Main Menu...")
                    return
                
                #  ELSE IF user input is 1:
                #  PRINT products list
                elif choice == 1:
                    print("Printing Product List...")
                    print_list(product_list)
                    print(input("Press 'Enter' to continue..."))

                #  ELSE IF user input is 2:
                # CREATE new product
                elif choice == 2:
                    while True:
                        create_item(product_list)

                        print("Would you like to add another?\n0: No\n1: Yes")
                        choice = get_input_int()
                        if choice == 0:
                            break
                    
                #  ELSE IF user input is 3:
                #STRETCH GOAL - UPDATE existing product
                elif choice == 3:               
                    while True:
                        try:
                            update_item(product_list)
                            break
                        except:
                            print('Update failed... Please enter valid index...')

                            
                #  ELSE IF user input is 4:
                #  # STRETCH GOAL - DELETE product
                if choice == 4:
                    delete_item(product_list)