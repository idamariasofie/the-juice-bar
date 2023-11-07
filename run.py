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
    print(f"Thanks for ordering juice number {data_str}")


get_order_data()
