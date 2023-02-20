import json


# MAIN MENU FUNCTION
def main_menu():
    menu_message = """\n\n<<< MAIN MENU OPTIONS >>>
1. ADD New Contact
2. FIND Contact
3. QUIT
\n[Enter the number] >>> """
    while True:
        menu_option = input(menu_message)
        if menu_option == '1':
            add_new_contact(load_phonebook())
        elif menu_option == '2':
            find_and_show_contacts(load_phonebook())
        elif menu_option == '3':
            print("\nGoodbye!")
            break
        else:
            print('!!! Please select <<< MENU OPTIONS >>> number !!!', 2 * '\n')


# EDIT/DELETE MENU FUNCTION
def edit_and_del_menu(f_id: int):
    edit_delete_message = ("""\n<<< WHAT TO DO WITH THIS CONTACT? >>>
    1. EDIT
    2. DELETE
    3. BACK to MAIN MENU
\n[Enter the number] >>> \n""")
    while True:
        menu_option = input(edit_delete_message)
        if menu_option == '1':
            contacts = load_phonebook()
            edit_contact(contacts, f_id)
            update_phonebook(contacts)
            break
        elif menu_option == '2':
            contacts = load_phonebook()
            delete_contact(contacts, f_id)
            update_phonebook(contacts)
            break
        elif menu_option == '3':
            break
        else:
            print('!!! Please select <<< OPTION >>> number !!!', 2 * '\n')


# LOAD DATA from JSON database
def load_phonebook(phonebook_path='./phonebook.json'):
    with open(phonebook_path, 'r') as f:  # load list with dictionaries from json-file
        contacts = json.load(f)
    return contacts


# SAVE NEW DATA to JSON database
def update_phonebook(contacts, phonebook_path='./phonebook.json'):
    with open(phonebook_path, 'w') as f:  # load list with dictionaries from json-file
        json.dump(contacts, f)


# 1) INPUT FIRST NAME FUNCTION
def input_firstname(default_value=None):
    if default_value is None:
        return input('First Name: >>> ')
    else:
        return input(f'First Name: {default_value}\n[Enter First Name] >>> ')


# 2) INPUT LAST NAME FUNCTION
def input_lastname(default_value=None):
    if default_value is None:
        return input('Last Name: >>> ')
    else:
        return input(f'Last Name: {default_value}\n[Enter Last Name] >>> ')


# 3) INPUT ADDRESS FUNCTION
def input_state(default_value=None):
    if default_value is None:
        return input('State: >>> ')
    else:
        return input(f'State: {default_value}\n[Enter State] >>> ')


# 4) INPUT PHONE FUNCTION
def input_phone(default_value=None):
    while True:
        if default_value is None:
            phone = input('Phone Number: >>> ')
        else:
            phone = input(f'Phone Number:{default_value}\n[Phone Number] >>> ')

        if phone == "":
            return default_value
        elif phone.isdigit():
            return phone
        else:
            print('!!! PLEASE ENTER DIGITS !!!\n')


# GET IDs list comprehension from contacts
def contacts_to_ids(contacts: list) -> list:
    return [dict_.get("id") for dict_ in contacts]


# Create NEW contact ID
def find_new_contact_id(contacts: list):
    existing_id_list = contacts_to_ids(contacts)
    return max(existing_id_list) + 1


# Create NEW CONTACT fUNCTION
def create_new_contact(new_id: int):
    new_contact = {"id": new_id,
                   "firstName": input_firstname(),
                   "lastName": input_lastname(),
                   "address": input_state(),
                   "phone": input_phone()}
    for key in new_contact.keys():
        if new_contact[key] == "" or new_contact[key] is None:
            new_contact[key] = "Unknown"
    return new_contact


# ADD (save) created NEW CONTACT FUNCTION
def add_new_contact(contacts: list):
    new_id = find_new_contact_id(contacts)
    new_contact = create_new_contact(new_id)

    save_message = """\n\n<<< SAVE THIS CONTACT ? >>>
1. YES
2. NO
\n[Enter the number] >>> """
    while True:
        menu_option = input(save_message)
        if menu_option == '1':
            contacts.append(new_contact)
            update_phonebook(contacts)
            print(f'\n!!! CONTACT was SAVED !!!\n')
            break
        elif menu_option == '2':
            break
        else:
            print('!!! Please select <<< OPTION >>> number !!!', 2 * '\n')


# SEARCHING FUNCTION
def filter_contacts(contacts: list, search: str) -> list:
    input_elements = search.lower().split()

    found_contacts = []
    for contact in contacts:
        # create list of dict values in lower case
        contact_values_low = [val.lower() for val in list(contact.values())[1:]]

        match = True
        for element in input_elements:
            if element not in contact_values_low:
                match = False
                break

        if match:
            found_contacts.append(contact)
    return found_contacts


# PRINTING FUNCTION of found contacts
def print_contacts_list(contacts: list):
    for contact in contacts:
        print(f"""id: {contact.get("id")}
            First Name: {contact.get("firstName")}
            Last Name: {contact.get("lastName")}
            State: {contact.get("address")}
            Phone Number: {contact.get("phone")}\n""")


# FIND and SHOW contacts
def find_and_show_contacts(contacts: list):
    search_input = input('\nSEARCH CONTACT >>> ')
    found_contacts = filter_contacts(contacts, search_input)
    found_contacts_ids = contacts_to_ids(contacts)
    print_contacts_list(found_contacts)

    if len(found_contacts) > 0:
        while True:
            try:
                f_id = int(input('[Enter founded contact ID] >>> '))
            except (TypeError, ValueError):
                print('!!! You MADE a MISTAKE! Please TRY AGAIN !!!\n')
                continue
            if type(f_id) == int and f_id in found_contacts_ids:
                edit_and_del_menu(f_id)  # call function
                break
            else:
                print('!!! You enter a WRONG Contact ID !!!\n')
    else:
        print('!!! CONTACT NOT FOUND !!!')


# DELETE CONTACT FUNCTION
def delete_contact(contacts: list, f_id: int):
    [contacts.remove(contact) for contact in contacts if f_id == contact["id"]]
    print('!!! Contact was DELETED !!!')


# EDIT CONTACT FUNCTION
def edit_contact(contacts: list, f_id: int):
    for contact in contacts:
        if f_id != contact["id"]:
            continue
        first_name = input_firstname(contact.get("firstName"))
        if first_name != "":
            contact["firstName"] = first_name
        last_name = input_lastname(contact.get("lastName"))
        if last_name != "":
            contact["lastName"] = last_name
        state = input_state(contact.get("address"))
        if state != "":
            contact["address"] = state
        phone = input_phone(contact.get("phone"))
        contact["phone"] = phone
    print(f'\n!!! CHANGES have been SAVED !!!')


if __name__ == "__main__":
    main_menu()
