contacts = []


def add_contact(name, phone, email):
    new_contacts = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(new_contacts)

    print("Contact added successfully!")


def view_contacts():
    if contacts == []:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(
                f"Name: {contact["name"]} | Phone: {contact["phone"]} | Email: {contact["email"]}")


def search_contact(name):
    found = False
    for contact in contacts:
        if contact["name"] == name:
            print(
                f"Name: {contact["name"]} | Phone: {contact["phone"]} | Email: {contact["email"]}")
            found = True
    if found == False:
        print("Contact not found.")


def delete_contact(name):
    found = False
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            found = True
            print("Contact deleted successfully.")
    if found == False:
        print("Contact not found.")


while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(name, phone, email)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Name: ")
        search_contact(name)
    elif choice == "4":
        name = input("Name: ")
        delete_contact(name)
    elif choice == "5":
        print("Ha det bra 💕")  # windows + . to find emojis
        break
