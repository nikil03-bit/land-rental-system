# Land Rental System – Console Application in Python 🏡

A feature-rich command-line project that allows users to rent and return available land parcels based on data stored in a `.txt` file. The system handles partial rentals, updates land availability, logs rental history, and generates uniquely timestamped billing receipts.

## 🔧 Features
- View land availability with details (Kitta No., City, Direction, Area, Zoning, Charge, Status)
- Rent land by selecting area (Anna) and duration (in months)
- Return rented land to make it available again
- Prevent double renting by auto-updating availability
- Generates uniquely named rental bills in `.txt` format
- Saves transaction history in `rented.txt`

## 🗂 File Overview
- `main.py`: Main logic for renting, returning, and billing land transactions.
- `land.txt`: Contains all available land listings.
- `rented.txt`: Transaction history log (auto-appended).
- `bill_<name>_<timestamp>.txt`: Auto-generated invoice file for each transaction.




