# Email Notification
This Python script connects to a SQL Server database, retrieves data using three different SQL queries, and sends an email notification if there are potential errors in online sales data. The script is designed to be run periodically to keep track of the Different topics on sales data.

## Table of Contents
Prerequisites
Usage
Configuration
Email Notification
File Attachment
Prerequisites
Before using this script, make sure you have the following dependencies installed:

- Python
- Pandas
- pyodbc
- smtplib (for sending email)
- An SMTP server (e.g., Gmail) for sending email notifications

## Usage
Install the required Python libraries:

1. pip install pandas pyodbc
2. Configure the script with your database connection details, email settings, and file paths (see Configuration).

## Configuration
Before running the script, you need to configure it by setting various parameters:

### SQL Server Database Connection:
1. Server: Set the server name.
2. Database: Set the database name.
3. uid: Set the database username.
4. pwd: Set the database password.
   
### Email Configuration:
1. From: Set your name as the sender.
2. To: Set the recipient's email address.

### File Paths:
1. path: Set the local file path where the output Excel file will be saved.
2. filename: Set the name of the output Excel file.


## Email Notification
The script uses the smtplib library to send email notifications. It sends an email with a subject indicating potential errors in online sales data. The sender's name and recipient's email address can be customized in the script.

# LAST BUT NOT LEAST IMPORTANT, SET UP YOUR GMAIL ACCOUNT TO SEND THE EMAILS 

Here's a detailed guide:

## Create a Gmail Account:
If you don't already have a Gmail account, you'll need to create one. Go to Gmail and click on "Create account." Follow the instructions to set up your Gmail account, including choosing a username and password.

## Enable Less Secure Apps:
To send emails via SMTP (Simple Mail Transfer Protocol), you need to enable "Less Secure Apps" in your Gmail account settings. Keep in mind that Google considers this option less secure because it allows apps with your credentials to access your account.

## Go to Google Account settings.
Click on "Security" in the left sidebar.
Under "Less secure app access," click "Turn on access."
Generate an App Password (Recommended):
Instead of using your main Gmail password, it's more secure to generate an "App Password" for use with Python. This password is specific to the application (in this case, your Python script).

Under the "Signing in to Google" section in your Google Account settings, go to "App passwords."
Select "Mail" and "Other (Custom name)," and then give it a name like "Python Email Sender."
Click "Generate." You will receive a 16-character password; save this, as you won't be able to see it again.




