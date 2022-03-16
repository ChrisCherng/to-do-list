# To Do App

The "To Do" App is a console web application which runs in the Code Institute mock terminal on Heroku.

It provides the user with a simple interface to keep track of their tasks.

[Here is the live version of this application.](https://p3-to-do-list.herokuapp.com/)

![Screenshot of the site on screens to show responsiveness](/assets/images/responsive.png)


## Features

The application starts by asking the user which function to use. The following flowchart shows the options that the user can select, as well as a summary of the functionality. This flowchart was created at the planning stage to assist with the coding.

![Flowchart of options for the to-do application](/assets/images/planningflow.PNG)

When selecting a function, the application will validate that the responses are suitable. If not, an error message will display, and the question will be asked again. As part of this, when selecting a function, the user may use any combination of upper or lower cases - this will ensure the user does not have to use the exact case when typing their response for ease of use.

### Add a New Task

The user inputs the name of the task, followed by the deadline of the task. The application will then add this new task to the listing, with a new number. This ensures every task has a unique number, which assists with the deletion and completion functions (below). This new task is added to the list with the default "Incomplete" status.

The application verifies if the user has input the deadline date in the correct format - if not, an error message will display and request a correct format date.

![Screenshot of the console when adding a task](/assets/images/addtask.png)

### Delete an Existing Task

The user inputs the unique number of the task that they would like to delete (to find this, they can use the view full list functionality). This will permenantly remove the task from the list, and therefore it will no longer appear on any of the view functionalities.

![Screenshot of the console when deleting a task](/assets/images/deletetask.png)

### Change the Name/Date of an Existing Task

The user inputs the task number they'd like to change. The application then asks for the updated name of the task and the updated deadline date. THis will overwrite this task in the list.

![Screenshot of the console when changing a task](/assets/images/changetask.png)

### Mark a Task as Complete

The user inputs the unique number of the task that they would like to mark as completed (to find this, they can use the view full list functionality). This will set the task status to "Complete".

![Screenshot of the console when completing a task](/assets/images/completetask.png)

### View the Full Listing

This will display the full list of all tasks on the list - both complete and incomplete. This includes the number of each task, which is used for the delete and complete functions.

![Screenshot of the full to-do list output](/assets/images/fullview.png)

### View a Summary Listing

This will display two summary tables of incomplete tasks:
- all overdue tasks; and
- the next three tasks due by date.

If there are no overdue tasks, the first table will display a message stating that there are no overdue tasks.
If there are fewer than three upcoming incomplete tasks in the list, the second table will only show as many as exist. If there are no upcoming tasks, a message will display that there are no upcoming tasks.

![Screenshot of the summary to-do list output](/assets/images/summaryview.png)


## Data Model

The data model for this application uses Google Sheets. The application is linked to a Google Sheets document that holds the information for the to-do list.

To perform any manipulation of the spreadsheet, including adding data, deleting data and amending data, the [gspread API](https://docs.gspread.org/en/latest/#) has been utilised. 

The manipulation required to extract the relevant overdue and upcoming information in the Summary View is performed within the code with the help of the [datetime API](https://docs.python.org/3/library/datetime.html).

![Screenshot of the underlying Google Sheets document](/assets/images/googlesheet.png)

## Testing

### Manual Testing

- Manual use cases have been run to test the functionality of the application.
- The table below shows the user stories, the associated use cases, the task script followed for the test, and whether this passed or failed.

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 001:** I want to be able to view the tasks that are on the list, so that I can review upcoming tasks as well as the history of tasks. | PASS |
| + > **Use Case 001-001:** I want to be able to view every task in the list, both complete and incomplete. | PASS |
| + + + > **Task 1:** Open the Heroku App -> the prompt "Would you like to view or amend the list?" should be displayed -> type in "View" and press Enter -> the prompt "Which view would you like?" should be displayed -> type "Full" and press Enter -> the full list will display | PASS |
| + > **Use Case 001-002:** I want to be able to view a summary of tasks, so that I can prioritise these. | PASS |
| + + + > **Task 1:** Open the Heroku App -> the prompt "Would you like to view or amend the list?" should be displayed -> type in "View" and press Enter -> the prompt "Which view would you like?" should be displayed -> type "Summary" and press Enter -> a list of overdue tasks, and a list of the next three due tasks (by date) will display. | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 002:** I want to be able to be able to add or delete tasks on the list. | PASS |
| + > **Use Case 002-001:** I want to be able to add a new task to the list. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Add" and press Enter -> input a task name -> input a deadline date -> if successful, the application will display: "This task has been added as item number X" where "X" is the next number along -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the new task has been added to this list at the end. | PASS |
| + > **Use Case 002-002:** The new task must have a unique number. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Add" and press Enter -> input a task name -> input a deadline date -> if successful, the application will display: "This task has been added as item number X" where "X" is the next number along -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the new task has a unique number compared to the previously existing tasks. | PASS |
| + > **Use Case 002-003:** I want to be able to delete tasks on the list if they are no longer applicable. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Delete" and press Enter -> select a task number (obtained from the "View" function first if required) -> if successful, the application will display: "Task number X has been deleted!" where "X" is the task number selected -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the selected task is no longer on the list. | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 003:** I want to be able to be able to amend existing tasks on the list. | PASS |
| + > **Use Case 003-001:** I want to be able to mark a task as Completed. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Complete" and press Enter -> select a task number that is status "Incomplete" (obtained from the "View" function first if required) -> if successful, the application will display: "Task number X has been set to Complete!" where "X" is the task number selected -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the selected task has a "Complete" status. | PASS |
| + + + > **Task 2:** Open the Heroku App -> type in "Amend" and press Enter -> type "Complete" and press Enter -> select a task number that is status "Complete" (obtained from the "View" function first if required) -> if successful, the application will display: "Task number X has been set to Complete!" where "X" is the task number selected -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the selected task continues to have a "Complete" status. | PASS |
| + > **Use Case 003-002:** I want to be able to amend the task name and/or deadline date. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Change" and press Enter -> select a task number (obtained from the "View" function first if required) -> the application will display: "Type the updated task name" -> type in an updated task name and press Enter -> the application will display: "What is the revised deadline for this updated task?" -> type in an updated deadline date and press Enter -> if successful, the application will display: "Task number X has been updated!" where "X" is the task number selected -> type "Full" and press Enter -> the full list will display -> verify that the selected task has the updated name and date. | PASS |

### "Negative Testing"

Negative testing was undertaken to determine whether the application could handle unwanted or unexpected user input. The following were performed:

- Tested using different combinations of upper and lower case for the selector inputs "view", "amend", "full", "summary", "add", "delete", "complete", and "change" at their respective points in the application flow. All tested combinations of upper and lower cases (e.g. "View", "VIEW", "view") provided the correct outcome with the application flow continuing as expected.
- Tested inputting selectors that are different to those specified (e.g. inputting "hello" at the first input prompt). Testing these inputs at all stages of the application flow resulted in the application clearly displaying the error, and the prompt requesting a correct input again. This is the expected outcome.
- Tested inputting a task number that does not exist during the "delete", "complete" and "change" functionality. This resulted in the application stating that the task number did not exist, then repeating the request to input a task number. Therefore, a user cannot perform task list amends for a task that does not exist.
- Testing inputting a date in the wrong format (e.g. 31-07-22) or does not exist (e.g. 31/02/2023) in the "add" or "change" functionality. In these tests, the application requested that the user input a valid date in the correct format DD/MM/YYYY, and repeats the input request. This ensures that the dates input are all consistently in the same format, which allows for the sorting being performed in the summary view functionality.
- Testing a task name with a very long name. The Code Institute mock terminal has a limit of 80 characters per line, and therefore any outputs displayed in the mock terminal must be below 80 characters. Some long task names were tested as part of the "add" and "change" functionalities. When the number of characters was over 20, an error message was displayed stating that the name should be below 20 characters, and the input prompt repeated. Therefore the number of characters on a line in the mock terminal will not exceed 80 characters, and any such information will be correctly displayed.

### Bugs

#### Fixed Bugs

- Tasks with longer names would not be able to be viewed on the console output. A validation function has been added to ensure the task names are no longer than 20 characters to ensure the correct output views.
- There were no error messages if you input a task that does not exist in the "delete task" function. This was unclear to users as to what happened. A validation function has been included to ensure that only existing task numbers can be used.
- If there were fewer than three overdue or upcoming tasks, the summary tables would not run correctly. Additional "if statement" codes have been implemented to ensure that the tables will run and display correctly in these cases.

### Code Validator Testing

PEP8:
- No errors were returned from [PEP8online.com](pep8online.com)

![PEP8 screenshot showing no errors](/assets/images/pep8.png)


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
- Gaff on the Code Institute Slack, for the format of the Testing section of the ReadMe.