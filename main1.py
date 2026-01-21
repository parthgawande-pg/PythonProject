# Lab Assignment 2: Vendor Annual Purchase Report

# Input vendor details
vendor_name = input("Enter Vendor Name: ")
year_of_association = int(input("Enter Year of Association: "))
contact_number = input("Enter Contact Number: ")
email_id = input("Enter Email ID: ")

annual_purchase = 0

print("\nEnter Monthly Purchase Amounts:")

# Read monthly purchase details
for month in range(1, 13):
    amount = float(input(f"Month {month} Purchase Amount: "))
    annual_purchase += amount

# Display annual report
print("\n--- Vendor Annual Purchase Report ---")
print("Vendor Name:", vendor_name)
print("Year of Association:", year_of_association)
print("Contact Number:", contact_number)
print("Email ID:", email_id)
print("Total Annual Purchase Amount:", annual_purchase)