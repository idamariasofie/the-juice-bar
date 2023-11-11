import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_juice_bar')


def get_order_data():
    """
    Get juice order value input from the user
    """
    while True:
        print("Welcome to The Juice Bar's order system")
        print("Please enter your juice of choice (1-5)")
        print("Then press Enter when you are ready.\n")

        data_str = input("Enter your order here:\n")
        order_data = data_str.split(",")

        if validate_data(order_data):
            print("Thanks for your order")
            break

    return order_data

def get_size_data():
    """
    Get juice size value input from the user
    """
    while True:
        print("Here is our catalogue for sizes and prices")
        print("Please enter the code for you juice size choice (S,M,L)")
        print("Then press Enter when you are ready.\n")

        data_str = input("Enter your order here:\n")
        size_data = data_str.split(",")

        if validate_data(size_data):
            print("Thanks for your order")
            break

    return size_data

def validate_data(value):
    """
    Converts all string values into integers.
    Raises ValueError if strings cannot be converted into integers.
    Or if there aren't exactly 1 value.
    """
    try:
        [int(value) for value in value]
        if len(value) != 1:
            raise ValueError(
                f"Please enter a number (1-5)\n you entered {len(value)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True

def update_order_worksheet(data):
    """
    Update the order worksheet and adds a new row with the data provided.
    """
    print("Let's get to the next step...\n")
    order_worksheet = SHEET.worksheet("order")
    order_worksheet.append_row(data)
    print("Your order was updated successfully\n")

def main():
    """
    Run all program functions
    """
class JuiceOrder:
    """
    Creates an instance of JuiceOrder
    """
    def __init__(self, juice_type, size, price, quantity):
        self.juice_type = juice_type
        self.size = size
        self.price = price
        self.quantity = quantity

data = get_order_data()
order_data = [int(num) for num in data]
update_order_worksheet(order_data)
size = get_size_data()

main()
