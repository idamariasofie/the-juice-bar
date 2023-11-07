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
    print("Please enter your juice of choice (1-5)")
    print("Then press Enter when you are ready\n")

    data_str = input("Enter your order here:")
    
    order_data = data_str.split(",")
    validate_data(order_data)

def validate_data(value):
    """
    Converts all string values into integers.
    Raises ValueError if strings cannot be converted into integers.
    Or if there are more then 1 value. 
    """
    try: 
        if len(value) != 1:
            raise ValueError(f"Please enter a number between 1-5, you provided {len(value)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")


get_order_data()
