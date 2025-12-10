phonebook = {
    "Yunus" : "0547876897",
    "Issac" : "0542312576",
    "Ben" : "0246787998",
    "Yahya" : "023465788"
}

def add_contact(phonebook , name, number):
    if name in phonebook:
        print("Contact already exist")
    if number in phonebook.values():
        print("Number already exist")
    else:
        phonebook[name] = number
        print(f"Contact {name} added Successfully!")

def  remove_contact(phonebook , name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} removed Successfully!")
    else:
        print(f"Contact not found")
def search_contact(phonebook, name):
    if name in phonebook:
        print(f"{name} : {phonebook[name]}")
    else:
        print("Contact not found")
        
def display_contact(phonebook):
    if phonebook:
        print("All Contact")
        for name, number in phonebook.items():
            print(f"{name} : {number}")
    else:
        print("Phonebook is empty")        
                
while True:
    print("\n --- Phonebook Menu ---")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Show All Contact" )
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(phonebook, name , number)
    elif choice == "2":
        name = input("Enter contact name to remove: ")
        number = input("Enter contact number to remove: ")
        remove_contact(phonebook, name)
    elif choice == "3":
        name = input("Enter contact name to seacrh: ")
        search_contact(phonebook, name)
    elif choice == "4":
        display_contact(phonebook)
    elif choice == "5":
        print("Existing Phonebook .. Later!")
        
    
    else: 
        print("Invalid Choice! Please enter number (1 - 5)...")
    break
    
    
# add_contact(phonebook, "Ali", "0551234567")  
# add_contact(phonebook, "Ben", "0246787998") 
# add_contact(phonebook, "Hassan", "0547876897") 
# remove_contact(phonebook, "Issac" )
# search_contact(phonebook, "Ali")
# display_contact(phonebook)