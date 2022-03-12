# To Do App

The "To Do" App is a console web application which runs in the Code Institute mock terminal on Heroku.

It provides the user with a simple interface to keep track of their tasks.

[Here is the live version of this application.](https://p3-to-do-list.herokuapp.com/)


## Features

The application starts by asking the user which function to use. The following flowchart shows the options that the user can select, as well as a summary of the functionality. This flowchart was created at the planning stage to assist with the coding.

![Flowchart of options for the to-do application](/assets/images/planningflow.PNG)

When selecting a function, the application will validate that the responses are suitable. If not, an error message will display, and the question will be asked again.

### Add a New Task

The user inputs the name of the task, followed by the deadline of the task. The application will then add this new task to the listing, with a new number. This ensures every task has a unique number, which assists with the deletion and completion functions (below). This new task is added to the list with the default "Incomplete" status.

The application verifies if the user has input the deadline date in the correct format - if not, an error message will display and request a correct format date.

### Delete an Existing Task

The user inputs the unique number of the task that they would like to delete (to find this, they can use the view full list functionality). This will permenantly remove the task from the list, and therefore it will no longer appear on any of the view functionalities.

### Mark a Task as Complete

The user inputs the unique number of the task that they would like to mark as completed (to find this, they can use the view full list functionality). This will set the task status to "Complete".

### View the Full Listing

This will display the full list of all tasks on the list - both complete and incomplete. This includes the number of each task, which is used for the delete and complete functions.

### View a Summary Listing

This will display two summary tables of incomplete tasks:
- all overdue tasks; and
- the next three tasks due by date.


## Data Model

The data model for this application uses Google Sheets. The application is linked to a Google Sheets document that holds the information for the to-do list.

To perform any manipulation of the spreadsheet, including adding data, deleting data and amending data, the [gspread API](https://docs.gspread.org/en/latest/#) has been utilised. 

The manipulation required to extract the relevant overdue and upcoming information in the Summary View is performed within the code with the help of the [datetime API](https://docs.python.org/3/library/datetime.html).

## Testing

### Manual Testing


### Bugs

### Validator Testing

PEP8:
- No errors were returned from [PEP8online.com](pep8online.com)


## Deployment

This application was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
- Fork or clone of the GitHub repository.
- Create a new Heroku app.
- Set the buildbacks to Python and NodeJS in that order.
- Link the Heroku app to the GitHub repository.
- Select "Deploy".


## Credits
- Code Institute for the GitHub template for terminal applications.
- [Pretty Table](https://pypi.org/project/prettytable/) to neatly format the table outputs to the console.
- [Pyfiglet](https://github.com/pwaller/pyfiglet) for the ASCII header.
- [LucidChart](https://www.lucidchart.com/pages/) for the flowcharts used in the planning stage.
- My mentor, Victor Miclovich, for his valuable insights, feedback and advice.
- My partner, Scott, for his support throughout the project.
- My family and friends for user testing and feedback.