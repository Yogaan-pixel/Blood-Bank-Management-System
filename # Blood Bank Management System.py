# Blood Bank Management System
# this is a simple blood bank management system 
# this will allow users to add donors, view donor list, search blood availability, add blood units, issue blood, and view current blood stock.    
#***********************************start of program********************************
# giving stock of blood groups

blood_stock = {
    "A+": 5,
    "A-": 2,
    "B+": 4,
    "B-": 2,
    "AB+": 3,
    "AB-": 1,
    "O+": 6,
    "O-": 2
}

donors = []



def get_positive_number(message):
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number
            else:
                print("Please enter a positive number.")


        except ValueError:
            print("Please enter a valid number.")

# function to add a donor

def add_donor():
    print("----------------------- Add Donor ---------------------------")

    name = input("Donor name: ").strip()
    age = get_positive_number("Donor age: ")
    blood_group = input("Blood group (example: A+): ").upper().strip()
    phone = input("Phone number: ").strip()

    if blood_group not in blood_stock:
        print("That blood group is not valid. Please try again.")
        return

    new_donor = {
        "name": name,
        "age": age,
        "blood_group": blood_group,
        "phone": phone
    }

    donors.append(new_donor)
    blood_stock[blood_group] += 1

    print(name," was added successfully.")
    print("One unit of", blood_group, "blood was added to stock.")

# function to show donors

def show_donors():
    print("----------------------- Donor List ---------------------------")

    if  len(donors) == 0:
        print("There are no donors registered yet.")
        return

    for number, donor in enumerate(donors, start=1):
        print("Donor ", number)
        print("Name        : ", donor['name'])
        print("Age         : ", donor['age'])
        print("Blood Group : ", donor['blood_group'])
        print("Phone       : ", donor['phone'])

#function to search blood availability

def search_blood():
    print("------------------- Search Blood Availability ---")

    blood_group = input("Enter blood group: ")
    blood_group = blood_group.upper()
    blood_group = blood_group.strip()
    if blood_group not in blood_stock:
        print("That blood group is not valid.")
        return

    available_units = blood_stock[blood_group]
    print(blood_group, "blood available:", available_units, "unit(s)")

#function to add blood units

def add_blood():
    print("--------------- Add Blood Units ---------------------------")

    blood_group = input("Enter blood group: ").upper().strip()

    if blood_group not in blood_stock:
        print("That blood group is not valid.")
        return

    units = get_positive_number("How many units would you like to add? ")
    blood_stock[blood_group] += units

    print(units,"unit(s) of",blood_group," blood added successfully.")

#function to issue blood

def issue_blood():
    print("----------------------- Issue Blood ---------------------------")

    blood_group = input("Enter blood group: ").upper().strip()

    if blood_group not in blood_stock:
        print("That blood group is not valid.")
        return

    units_needed = get_positive_number("How many units are needed? ")

    if blood_stock[blood_group] >= units_needed:
        blood_stock[blood_group] -= units_needed
        print("Blood issued successfully.")
    else:
        print("Not enough ",blood_group," blood available. Only" ,blood_stock[blood_group], "in stock.")

#function to show blood stock

def show_blood_stock():
    print("------------------------- Current Blood Stock ---------------------------------")

    for blood_group, units in blood_stock.items():
        print(blood_group, ": ", units, " unit(s)")

# main loop

while True:
    
    print("=============================================================================")
    print("--------------------------BLOOD BANK MANAGEMENT------------------------------")
    print("=============================================================================")
    print("1 - Add a donor")
    print("2 - View donor list")
    print("3 - Search blood availability")
    print("4 - Add blood units")
    print("5 - Issue blood")
    print("6 - View blood stock")
    print("7 - Exit")
    choice = input("Choose an option : ")
    if choice == "1":
        add_donor()
    elif choice == "2":
        show_donors()
    elif choice == "3":
        search_blood()
    elif choice == "4":
        add_blood()
    elif choice == "5":
        issue_blood()
    elif choice == "6":
        show_blood_stock()
    elif choice == "7":
        break
    else:
        print("Invalid option ")

#****************************end of program********************************
#                                                              -by s.yogaan