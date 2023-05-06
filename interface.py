

def validate_to_int(str_input):
    while True:
        try:
            user_input = input(str_input)
            return int(user_input)
        except:
            print("Please enter a number.")
        pass


