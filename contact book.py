contacts = []

def add_contact(name, phone, email, address):
    contacts.append({"name":name , "phone":phone , "email":email , "address":address})
    print ("contacts added successfully ")

def view_contacts():
    if contacts:
        for contact in contacts :
            print(f"name: {contact['name']}, phone: {contact['phone']}")
    else:
        print("no contacts available")

def search_contact(keyword):
    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print(f"name : {contact['name']} , phone: {contact['phone']}")
            found = True
    if not found:
        print("contact not found")

def update_contact(name, phone, email, address):
    for contact in contacts:
        if contact['name'] == name:
            contact.update({"phone":phone , "email":email , "address": address})
            print ("contact updated successfully")
            return
    print("contact not found")

def delete_contact(name):
    for contact in contacts:
        if contact['name'] ==name:
            contacts.remove(contact)
            print("contact deleted successfully")
            return
    print("contact not found")

while True:
    print("\n MENU:")
    print("1. Add contacts")
    print("2.View contact list")
    print("3.Search contact")
    print("4.Update contact")
    print("5.Delete contact")
    print("6.Exit")

    choice =input("enter your choice:")
    
    if choice =="1":
        name = input("enter name :")
        phone = input("enter phone number :")
        email = input("enter email id :")
        address = input("enter address :")
        add_contact(name, phone, email, address)
    
    elif choice == "2":
        print("contact list :")
        view_contacts()

    elif choice == "3":
        keyword = input("enter name or phone number to search :")
        search_contact(keyword)

    elif choice == "4":
        name = input("enter name of contact to update:")
        phone = input("enter new phone number:")
        email = input("enter new email id:")
        address = input("enter new address:")
        update_contact(name, phone, email, address)

    elif choice == "5":
        name = input("enter name of contact to delete:")
        delete_contact(name)

    elif choice == "6":
        print("exiting")
        break
    else:
        print("Invalid Choice . Please enter a number between 1 to 6")

