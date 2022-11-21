import csv
# #read from products
# with open(product_path, "r") as f:
#     reader = csv.DictReader(f)
#     product_list = list(reader)
#     #print (a)

# #read from courier
# with open(courier_path, "r") as f:
#     reader = csv.DictReader(f)
#     courier_list = list(reader)
#     #print (a)

# #read from orders
# with open(orders_path, "r") as f:
#     reader = csv.DictReader(f)
#     order_list = list(reader)
#     #print (a)

#function to "save" list to file
def write_list(list_name, list, path):
    
    print(f'Saving {list_name} to file at {path}')

    with open(path, 'w', newline='') as output_file:
        keys = list[0].keys()

        dict_writer = csv.DictWriter(output_file,keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)