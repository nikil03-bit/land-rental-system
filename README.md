
# Land Rental System – Console Application in Python 🏡

A simple command-line project that allows users to rent available land parcels based on details stored in a `.txt` file. The system updates land availability, calculates rent, and generates a bill.

## 🔧 Features
- View land availability with details (Kitta No., City, Direction, Area, Zoning, Charge, Status)
- Rent land by area and duration
- Prevent double renting (status updates after rent)
- Generates a printable bill
- Saves transaction history in a text file

## 🗂 File Overview
- `main.py`: Main logic for renting land, updating availability, and generating bills.
- `land.txt`: Contains all available land listings.
- `bill2.txt`: Output file (auto-generated) for rental receipt.

## 🔧 Technologies Used
- Python (Standard Library only)

## 🚀 How to Run
1. Clone the repo:
```bash
git clone https://github.com/yourusername/land-rental-system.git
cd land-rental-system
