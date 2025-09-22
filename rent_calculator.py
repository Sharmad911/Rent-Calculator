## Inputs we need from the user
# Total rent
# Total food ordered
# Electricity units spent
# Charge per unit
# Anount of people living the the room

## Output
# Total amount you've to pay is:

rent = int(input("Enter your rent: "))
food = int(input("Enter the amount of food ordered: "))
electricity_spend = int(input("Enter the total of electricity spend: "))
charge_per_unit = int(input("Enter the charge per unit: "))
persons = int(input("Enter the amount of people living in the room: "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons
print("Each person will pay: ", output)