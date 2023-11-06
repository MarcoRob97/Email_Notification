import smtplib
from email.message import EmailMessage
import pandas as pd
import pyodbc 


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=yourservername;'
                      'Database=yourdatabase;'
                      'uid=Yourusername;'
                      'pwd=yourpassword;'
                      'MARS_Connection=yes;')   

data_set1 = pd.read_sql_query('''
            
                select * from customers # here is your query 1

            ''', conn)


data_set2 = pd.read_sql_query('''
            	select * from customers # here is your query 2
            ''', conn)

data_set3 = pd.read_sql_query('''
            	select * from customers # here is your query 3
            ''', conn)

conn.close()

df1 = pd.DataFrame(data_set1)
df2 = pd.DataFrame(data_set2)
df3 = pd.DataFrame(data_set3)

msg=EmailMessage()
msg['Subject']='Possible ERRORS in online Sales'
msg['From']='Marco Andree Roblero'
msg['To']='marcorob@test.com'
#msg['To']=['marcorob@test.com', 'KarlaC@test.com','ElizabethH@test.com'] # you can create a list a past multiple receipients

path = "//yourpath/"
filename = "output.xlsx"

with pd.ExcelWriter(path + filename) as writer:
        df1.to_excel(writer, sheet_name='notification_1')
        df2.to_excel(writer, sheet_name='notification_2')
        df3.to_excel(writer, sheet_name='notification_3')
        
x = len(df2)
y = len(df1)
z = len(df3)

if x > 0 or y > 0 or z > 0:
    with open('//yourpath/output.xlsx', "rb") as f:
        file_data=f.read()
        file_path = '//yourpat/output.xlsx'
        file_name= file_path.split('/')[-1]
        print("File name is",file_name)
        msg.add_attachment(file_data,maintype="application",subtype="xlsx",filename=file_name)
        
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login("youremail@gmail.com","jvutpqhtoozebtfj")
        server.send_message(msg)

else:
    print('nothing today')
