import random


def password_gen():
    number = ""
    character = ""
    special = ""
    length = ""
    while True:
        try:
            length = int(input("Enter the the length(integers) of the password :"))
            break
        except ValueError:
            print("That's not a valid option!")
            return None
    number = input("Enter y/n if you want to your password to have numbers :")
    character = input("enter y/n if you want to your password to have character :")
    special = input("enter y/n if you want to your password to have special_list character :")
    digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    characters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                       'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                       'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                       'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                       'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                       'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                       'Z']
    special_list = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                    '*', '(', ')', '<']
    combined_list = []
    if number == character == special == 'y':  # 1 1 1
        combined_list = digits_list + characters_list + special_list
    elif number == character == 'y' and special == 'n':  # 1 1 0
        combined_list = digits_list + characters_list
    elif number == 'y' and character == special == 'n':  # 1 0 0
        combined_list = digits_list
    elif (number == special == 'y') and (character == 'n'):  # 1 0 1
        combined_list = digits_list + special_list
    elif number == character == 'n' and special == 'y':  # 0 0 1
        combined_list = special_list
    elif number == special == 'n' and character == 'y':  # 0 1 0
        combined_list = characters_list
    elif number == 'n' and character == special == 'y':  # 0 1 1
        combined_list = characters_list + special_list
    elif number == character == special == 'n':  # 0 0 0
        combined_list = characters_list + special_list
        print("We can't generate password")
        return None
    else:
        print("wrong input is entered try again")
        return None
    random.shuffle(combined_list)
    password = ""
    for i in range(int(length)):
        password = random.choice(combined_list) + password
    print(password)


password_gen()
