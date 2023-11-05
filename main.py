def choose_key(dob):
    # max key is 159
    # 12+31+99=142
    key = 0
    month = dob[0] + dob[1]
    day = dob[2] + dob[3]
    year = dob[6] + dob[7]
    key = int(month) + int(day) + int(year)
    return key


def create_profile(name, dob, key, passw):
    encrypted_string = ''

    for n in name:
        ascii_int = ord(n)
        encrypted_symbol = ascii_int ^ key
        ascii_rep = chr(encrypted_symbol)
        encrypted_string += ascii_rep

    name = encrypted_string

    encrypted_string = ''

    for n in dob:
        ascii_int = ord(n)
        encrypted_symbol = ascii_int ^ key
        ascii_rep = chr(encrypted_symbol)
        encrypted_string += ascii_rep

    dob = encrypted_string

    encrypted_string = ''

    for n in passw:
        ascii_int = ord(n)
        encrypted_symbol = ascii_int ^ key
        ascii_rep = chr(encrypted_symbol)
        encrypted_string += ascii_rep

    passw = encrypted_string

    f = open("profile.txt", "w")
    f.write(name + '\n' + dob + '\n' + passw + '\n' + str(key))
    f.close()


def delete_passwords():
    f = open("passwords.txt", "w")
    f.write('')
    f.close()


def delete_profile():
    f = open("profile.txt", "w")
    f.write('')
    f.close()


def encrypt(string, key):
    encrypted_string = ''

    for n in string:
        ascii_int = ord(n)
        encrypted_symbol = ascii_int ^ key
        ascii_rep = chr(encrypted_symbol)
        encrypted_string += ascii_rep

    return encrypted_string


def load_passwords():
    f = open("passwords.txt", "r")
    s = f.read()
    a = 0

    while a == 0:
        if s == '':
            a = 1

        print(s)
        s = f.read()


def select_substring(string, key):
    start = key % 5
    return string[start:start+3]


if __name__ == '__main__':
    input_key = ''
    name_of_user = ''
    dob_of_user = ''
    encryption_key = 0
    unique_password = ''

    print("Press 'c' to create a profile")
    print("Press 'l' to load your profile")
    print("Press 'q' to quit the program (all created passwords are autosaved)")

    input_key = input()

    if input_key == 'c':
        print("Enter your FULL name: ")
        name_of_user = input()

        print("Enter your date of birth (MMDDYYYY) : ")
        dob_of_user = input()

        print('\n')
        encryption_key = choose_key(dob_of_user)

        print("Enter your unique password for encrypting: ")
        unique_password = input()
        unique_password += select_substring(name_of_user, encryption_key)
        # print(unique_password)
        create_profile(name_of_user, dob_of_user, encryption_key, unique_password)

        while input_key != 'q':
            print("Press 'n' to create an new encrypted password for a website")
            print("Press 'l' to load all passwords you have for websites")
            print("Press 'd' to delete all passwords from your list")
            print("Press 'q' to quit the program (all created passwords are autosaved)")
            input_key = input()

            if input_key == 'n':
                print("Type the name of the site you want a password")
                new_site_name = input()
                print(unique_password)
                save_string = unique_password
                file = open("passwords.txt", "a")
                file.write(save_string)
                save_string = encrypt(new_site_name, encryption_key)
                file.write(save_string + '\n----------\n')
                file.close()

            if input_key == 'l':
                load_passwords()

            if input_key == 'd':
                print("Are you sure you want to delete ALL of your passwords (y or n)?")
                input_key = input()

                if input_key == 'y':
                    delete_passwords()

            if input_key != 'n' or input_key != 'l' or input_key != 'd' or input_key != 'q':
                print("Invalid character. Please enter either an 'n', 'l', 'd' or 'q'")

    if input_key == 'l':
        file = open("profile.txt", "r")
        name_of_user = file.readline()
        dob_of_user = file.readline()
        unique_password = file.readline()
        encryption_key = int(file.readline())
        file.close()

        print(unique_password)
        while input_key != 'q':
            print("Press 'n' to create an new encrypted password for a website")
            print("Press 'l' to load all passwords you have for websites")
            print("Press 'd' to delete a password from your list")
            print("Press 'q' to quit the program (all created passwords are autosaved)")
            input_key = input()

            if input_key == 'n':
                print("Type the name of the site you want a password")
                new_site_name = input()
                print(unique_password)
                save_string = unique_password
                file = open("passwords.txt", "a")
                file.write(save_string)
                save_string = encrypt(new_site_name, encryption_key)
                file.write(save_string + '\n----------\n')
                file.close()

            if input_key == 'l':
                load_passwords()

            if input_key == 'd':
                print("Are you sure you want to delete ALL of your passwords (y or n)?")
                input_key = input()

                if input_key == 'y':
                    delete_passwords()

            if input_key != 'n' or input_key != 'l' or input_key != 'd' or input_key != 'q':
                print("Invalid character. Please enter either an 'n', 'l', 'd' or 'q'")

    if input_key == 'q':
        quit()

