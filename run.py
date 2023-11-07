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
    Get order value input from the user
    """
    while True:
        print("Please enter your juice of choice (1-5)")
        print("Then press Enter when you are ready.\n")

        data_str = input("Enter your order here:\n")
        order_data = data_str.split(",")

        if validate_data(order_data):
            print("Thanks for your order")
            break

    return order_data

def validate_data(value):
    """
    Converts all string values into integers.
    Raises ValueError if strings cannot be converted into integers.
    Or if there are more then 1 value.
    """
    try:
        [int(value) for value in value]
        if len(value) != 1:
            raise ValueError(
                f"Please enter a number 1-5, you entered {len(value)}")
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

data = get_order_data()
order_data = [int(num) for num in data]
update_order_worksheet(order_data)