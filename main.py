# Land Rental System with Additional Features
from datetime import datetime
import os
import re

land_info = {}
rented_kitta = []
time_list = []
rented_area = []


def read_land_data():
    try:
        with open("land.txt", "r") as file:
            for line in file:
                l = line.strip().split(",")
                land_info[l[0]] = l[1:]
    except FileNotFoundError:
        print("Error: 'land.txt' not found.")
        exit()


def write_land_data():
    with open("land.txt", "w") as file:
        for key, value in land_info.items():
            file.write(key + "," + ",".join(value) + "\n")


def display_land_details():
    print("Kitta No.\t City\t\t Direction\t Anna\t Zoning\t\t Charge(/month)\t Availability")
    for key, value in land_info.items():
        print(f"{key}\t\t {value[0]:<10} {value[1]:<10} {value[2]:<5} {value[3]:<10} {value[4]:<10} {value[5]}")


def rent_land():
    display_land_details()
    while True:
        kitta_no = input("\nEnter the Kitta No. you want to rent: ")
        if kitta_no in land_info and land_info[kitta_no][-1].strip().lower() == 'available':
            break
        print("Invalid or unavailable Kitta No. Please try again.")

    total_anna = int(land_info[kitta_no][2])
    while True:
        anna = input(f"Enter the area (anna) to rent (Max {total_anna}): ")
        if anna.isdigit() and 0 < int(anna) <= total_anna:
            break
        print("Invalid area. Please enter a valid portion.")

    while True:
        months = input("Enter the number of months you want to rent: ")
        if months.isdigit() and int(months) > 0:
            break
        print("Please enter a valid number of months.")

    print(f"You are about to rent Kitta No. {kitta_no} for {months} months and {anna} anna.")
    confirm = input("Confirm? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Rental cancelled.")
        return

    remaining_anna = total_anna - int(anna)
    land_info[kitta_no][2] = str(remaining_anna)
    if remaining_anna == 0:
        land_info[kitta_no][-1] = 'Not Available'

    rented_kitta.append(kitta_no)
    time_list.append(months)
    rented_area.append(anna)
    write_land_data()
    log_rental(kitta_no, anna, months)
    print(f"Land with Kitta No. {kitta_no} rented successfully!\n")


def log_rental(kitta_no, anna, months):
    with open("rented.txt", "a") as f:
        now = datetime.now()
        f.write(f"{kitta_no},{anna},{months},{now}\n")


def return_land():
    display_land_details()
    kitta_no = input("Enter the Kitta No. you want to return: ")
    if kitta_no in land_info and land_info[kitta_no][-1].strip().lower() == 'not available':
        total_anna = int(input("Enter how many anna to return: "))
        land_info[kitta_no][2] = str(int(land_info[kitta_no][2]) + total_anna)
        land_info[kitta_no][-1] = 'Available'
        write_land_data()
        print(f"Land with Kitta No. {kitta_no} has been returned.\n")
    else:
        print("Invalid Kitta No. or land is already available.")


def generate_bill(name, phone):
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    invoice_id = f"TPN{timestamp}"
    filename = f"bill_{name}_{timestamp}.txt"

    total_rent = 0
    with open(filename, "w") as f:
        f.write(f"Invoice ID: {invoice_id}\nTechno Property Nepal\nKalopul, Kathmandu\n")
        f.write(f"Customer: {name}\nPhone: {phone}\nDate: {now}\n")
        f.write("--------------------------------------------------\n")
        f.write("Kitta\tCity\tDirection\tAnna\tZoning\tCharge\tMonths\tTotal\n")

        for i, kitta_no in enumerate(rented_kitta):
            details = land_info[kitta_no]
            charge = int(details[4])
            months = int(time_list[i])
            anna = int(rented_area[i])
            subtotal = charge * months * anna / int(details[2]) if int(details[2]) > 0 else 0
            total_rent += subtotal
            f.write(f"{kitta_no}\t{details[0]}\t{details[1]}\t{anna}\t{details[3]}\t{charge}\t{months}\t{subtotal}\n")

        f.write("--------------------------------------------------\n")
        f.write(f"Grand Total: NPR {int(total_rent)}\n")
        f.write("Thank you for choosing us!\n")

    print(f"\nBill generated: {filename}\n")


def main():
    read_land_data()
    print("\nWelcome to Techno Property Nepal Land Rental System\n")
    while True:
        name = input("Enter your name: ")
        if re.match("^[A-Za-z ]+$", name):
            break
        print("Invalid name. Use letters only.")

    while True:
        phone = input("Enter your contact number: ")
        if phone.isdigit() and len(phone) == 10:
            break
        print("Invalid phone number. Must be 10 digits.")

    while True:
        print("\n1. Rent Land\n2. Return Land\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            rent_land()
            while input("Do you want to rent another land? (yes/no): ").lower() == "yes":
                rent_land()
            generate_bill(name, phone)
        elif choice == '2':
            return_land()
        elif choice == '3':
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid input. Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
