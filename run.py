import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('to_do_list')


def select_function():
    """
    Asks the user which function they want to use
    Between amending the list and viewing the list
    """
    while True:
        print("Would you like to view or amend the list?")

        function_response = input("Type 'View' or 'Amend' here: \n")
        if validate_select_function(function_response):
            break

    return function_response


def validate_select_function(response):
    """
    Checks that the user has input 'View' or 'Amend'
    Allows the user to input either upper or lower case
    """
    functions = ['view', 'amend']
    if response.lower() in functions:
        return True
    else:
        print("Response should be 'View' or 'Amend' only")
        return False


def select_view_function():
    """
    If the user has selected 'View' from the first question
    This function allows the user to select which type of view they would like
    """
    while True:
        print("Which view would you like?")

        view_response = input("Type 'Full' or 'Summary' here: \n")
        if validate_view_function(view_response):
            break

    return view_response


def validate_view_function(response):
    """
    Checks that the user has input 'Full' or 'Summary'
    Allows the user to input either upper or lower case
    """
    views = ['full', 'summary']
    if response.lower() in views:
        return True
    else:
        print("Response should be 'Full' or 'Summary' only")
        return False


def select_amend_function():
    """
    If the user has selected amend in the first question
    This function allows the user to select which type of amendment they would like to make
    """
    print("Test")


def view_full():
    """
    Formats and displays the full to-do list
    """
    data = SHEET.worksheet('to_do').get_all_values()
    full_list = PrettyTable()
    full_list.field_names = data[0]
    for i in range(len(data)-1):
        full_list.add_row(data[i+1])
    print(full_list)


def view_summary():
    """
    Formats and displays a summary of the list
    """
    print("Test")


if select_function().lower() == 'view':
    select_view_function()
elif select_function().lower() == 'amend':
    select_amend_function()

if select_view_function().lower() == 'full':
    view_full()
elif select_view_function().lower() == 'summary':
    view_summary()
