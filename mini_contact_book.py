contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == "2":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found!")

    elif choice == "3":
        name = input("Enter Name to Update: ")
        if name in contacts:
            contacts[name] = input("Enter New Phone Number: ")
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        if contacts:
            print("\nAll Contacts:")
            for name, phone in contacts.items():
                print(name, "-", phone)
        else:
            print("No Contacts Available.")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")