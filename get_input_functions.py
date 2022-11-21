
def get_input_int(request=False, range =False):
    while True:
        if request is not False:
            print(request)

        #Test if input() is valid
        try:
            choice = int(input())
            if range is not False:
                if choice > range:
                    print('Chosen number exeeds index range')
                    raise Exception("Index range exeeded")

            return choice
        except Exception as e:
            print("Error with input. Please only enter valid numbers...")
            input('press enter to continue...')
            break
    
def get_input_str(request=False):
    while True:
        if request is not False:
            print(request)
        #Test if input() is valid
        try:
            choice = input()
            
            return choice.lower()
        except Exception as e:
            print("Error with input...")
            input('press enter to continue...')
            
def get_input_bin(request=False):
    while True:
        if request is not False:
            print(request)
        #Test if input() is valid
        try:
            choice = bin(int(input()))
            
            
            return choice
        except Exception as e:
            print(str(e) + "\nError with input. Please only select 0 or 1...")
            input('press enter to continue...')