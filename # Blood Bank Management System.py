# Blood Bank Management System

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
    """Keep asking until the user enters a positive whole number."""
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")


def add_donor():
    print("\n--- Add Donor ---")

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

    print(f"\n{name} was added successfully.")
    print(f"One unit of {blood_group} blood was added to stock.")


def show_donors():
    print("\n--- Donor List ---")

    if not donors:
        print("There are no donors registered yet.")
        return

    for number, donor in enumerate(donors, start=1):
        print(f"\nDonor {number}")
        print(f"Name        : {donor['name']}")
        print(f"Age         : {donor['age']}")
        print(f"Blood Group : {donor['blood_group']}")
        print(f"Phone       : {donor['phone']}")


def search_blood():
    print("\n--- Search Blood Availability ---")

    blood_group = input("Enter blood group: ").upper().strip()

    if blood_group not in blood_stock:
        print("That blood group is not valid.")
        return

    available_units = blood_stock[blood_group]
    print(f"{blood_group} blood available: {available_units} unit(s)")


def add_blood():
    print("\n--- Add Blood Units ---")

    blood_group = input("Enter blood group: ").upper().strip()

    if blood_group not in blood_stock:
        print("That blood group is not valid.")
        return

    units = get_positive_number("How many units would you like to add? ")
    blood_stock[blood_group] += units

    print(f"{units} unit(s) of {blood_group} blood added successfully.")


def issue_blood():
    print("\n--- Issue Blood ---")

    blood_group = input("Enter blood group: ").upper().strip()

    if blood_group not in blood_stock:
        print("That blood group is not valid.")
        return

    units_needed = get_positive_number("How many units are needed? ")

    if blood_stock[blood_group] >= units_needed:
        blood_stock[blood_group] -= units_needed
        print(f"{units_needed} unit(s) of {blood_group} blood issued successfully.")
    else:
        print(f"Sorry, only {blood_stock[blood_group]} unit(s) of {blood_group} are available.")


def show_blood_stock():
    print("\n--- Current Blood Stock ---")

    for blood_group, units in blood_stock.items():
        print(f"{blood_group}: {units} unit(s)")


def show_menu():
    print("\n" + "=" * 35)
    print("     BLOOD BANK MANAGEMENT")
    print("=" * 35)
    print("1. Add a donor")
    print("2. View donor list")
    print("3. Search blood availability")
    print("4. Add blood units")
    print("5. Issue blood")
    print("6. View blood stock")
    print("7. Exit")


while True:
    show_menu()
    choice = input("\nChoose an option (1-7): ").strip()

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
        print("\nThank you for using the Blood Bank Management System.")
        break
    else:
        print("Invalid option. Please choose a number from 1 to 7.")