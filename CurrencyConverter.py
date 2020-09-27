# Currency Converter

# Dictionary to store the list of currently unit along with its values
currency = {}

# read the list stored in text file
with open('CurrencyConverter.txt') as f:
    line = f.readlines()

# split the data stored in text file and stored it in dictionary
for lines in line:
    lines = lines.split('\t')
    currency[lines[0]] = lines[1]

# user input the amount to be converted
user_input = int(input("Enter Amount: "))

# displays the list of all the conversion units available
print("Enter the name of the currency you want to convert in.Available options are: \n")
[print(items) for items in currency.keys()]
conversion_name = input('Please enter the name of conversion: ')

# calculates and displays the output
print(f"INR {user_input} is equal to {user_input * float(currency[conversion_name])} {conversion_name}")
