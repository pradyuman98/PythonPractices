'''import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('pradyumanpareek330@gmail.com', 'p8796350634')
server.sendmail('pradyumanpareek330@gmail.com',
'pradyumanpp1998@gmail.com',
'Hi Man, This is for testing'
)

server.quit()'''


import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Read Data File from syatem....
data = pd.read_excel("C:/Users/inparp00/Desktop/dataFile.xlsx")
print(type(data))

#print(data.get("email"))

listOfEmails = list(data.get("email"))
listOFNames =  list(data.get("name"))
#print(listOfEmails)


#To Send Emails
try:
    
    #Setting Up the Server
    server = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
    server.ehlo()
    server.login('info@allesexports.com', 'nahoR@321')

    #Setting Sender and Receiver
    from_ = 'info@allesexports.com'
    to_ = listOfEmails

    #Setting message (This can also contain Image)
    message = MIMEMultipart("alternative")

    #Defining subject
    message["Subject"] = "Proposal for scrap and non ferrous metals."
    message["from"] = 'info@allesexports.com'


#Writing message in HTML Format
    html = '''
    <html>
    <head></head>

    <body>
    

<p>Dear Sir/Madam,</p>
<p>I would like to inform you....</p>
<p>I will be pleased...</p>
<p>We hope to have.........</p>
<p>Looking forward to ........</p>

    </body>

    </html>
    
    '''

#Converting html to Text
    messagePart2 = MIMEText(html, "html")

#Attaching HTML part to message which was defined earlier
    message.attach(messagePart2)


#Sending message
    server.sendmail(from_,to_,message.as_string())

    print("Message Sent")


    server.quit()

except Exception as e:
    print(e)