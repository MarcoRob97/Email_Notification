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

-Python
-Pandas
-pyodbc
-smtplib (for sending email)
-An SMTP server (e.g., Gmail) for sending email notifications

## Usage
1.Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/MarcoRob97/Email_Notification.git
Install the required Python libraries:

bash
Copy code
pip install pandas pyodbc
Configure the script with your database connection details, email settings, and file paths (see Configuration).

Run the script:

bash
Copy code
python email_multiple_notications_and_receipients.py
The script will perform the following steps:

Connect to the specified SQL Server database.
Execute three SQL queries to retrieve data from your desired tables.

In my case i need it to notify in my company abouth specific anomalies, so if the requests of the views 
came with any result it will create and excel file, for your case this is optional.

## Configuration
Before running the script, you need to configure it by setting various parameters:

SQL Server Database Connection:

Server: Set the server name.
Database: Set the database name.
uid: Set the database username.
pwd: Set the database password.
Email Configuration:

From: Set your name as the sender.
To: Set the recipient's email address.
File Paths:

path: Set the local file path where the output Excel file will be saved.
filename: Set the name of the output Excel file.
Email Notification
The script uses the smtplib library to send email notifications. It sends an email with a subject indicating potential errors in online sales data. The sender's name and recipient's email address can be customized in the script.




