import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from datetime import datetime

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

    if function_response.lower() == 'view':
        select_view_function()
    else:
        select_amend_function()

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

    if view_response.lower() == 'full':
        view_full()
    else:
        view_summary()

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
    This function allows the user to select which type of amendment they want
    """
    while True:
        print("What amendment would you like?")

        amend_response = input("Type 'Add', 'Delete' or 'Complete' here: \n")
        if validate_amend_function(amend_response):
            break

    if amend_response.lower() == 'add':
        add_task()
    elif amend_response.lower() == 'delete':
        delete_task()
    else:
        complete_task()

    return amend_response


def validate_amend_function(response):
    """
    Checks that the user has input 'Add', 'Delete' or 'Complete'
    Allows the user to input either upper or lower case
    """
    amendments = ['add', 'delete', 'complete']
    if response.lower() in amendments:
        return True
    else:
        print("Response should be 'Add', 'Delete' or 'Complete' only")
        return False


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
    data = SHEET.worksheet('summary').get_all_values()
    summary_list = PrettyTable()
    summary_list.field_names = data[0]
    for i in range(len(data)-1):
        summary_list.add_row(data[i+1])
    print(summary_list)


def add_task():
    """
    Requests the user to input a new task
    Adds the task to the google sheet list at the end
    """
    new_input = input("Type the name of the task here: \n")
    print("What is the deadline for this new task?")
    new_date = input("Use the format DD/MM/YYYY?: \n")
    validate_add_task(new_date)

    list_worksheet = SHEET.worksheet('to_do')
    task_numbers = list_worksheet.col_values(1)
    task_numbers.remove('Number')
    task_numbers_int = list(map(int, task_numbers))

    new_index = max(task_numbers_int) + 1
    new_task = [new_index, new_input, new_date, 'Incomplete']
    list_worksheet = SHEET.worksheet('to_do')
    list_worksheet.append_row(new_task)

    print(f"This task has been added as item number {new_index}.")


def validate_add_task(date):
    """
    Validates that the date input by the user is in the correct format
    Will provide an error message if incorrect and request the date again
    """
    date_format = "%d/%m/%y"
    res = True
    try:
        res = bool(datetime.strptime(date, date_format))
    except ValueError:
        res = False

    return res


def delete_task():
    """
    Requests the user input a task number from the full table list
    Deletes the task from the google sheet
    """
    list_worksheet = SHEET.worksheet('to_do')
    task_numbers = list_worksheet.col_values(1)
    task_selection = input("Which task number would you like to delete? \n")
    task_position = int(task_numbers.index(task_selection))
    list_worksheet.delete_rows(task_position + 1)
    print(f"Task number {task_selection} has been deleted!")


def complete_task():
    """
    Requests the user input a task number from the full table list
    Sets the task status to Complete
    """
    list_worksheet = SHEET.worksheet('to_do')
    task_numbers = list_worksheet.col_values(1)
    task_selection = input("Which task number is complete? \n")
    task_position = int(task_numbers.index(task_selection))
    list_worksheet.update_cell(task_position + 1, 4, 'Complete')
    print(f"Task number {task_selection} has been set to Complete!")


select_function()