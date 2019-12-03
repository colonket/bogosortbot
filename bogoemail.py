import smtplib
from email.message import EmailMessage

import creds

with open ("fans.txt", "r") as file:
    fans=file.readlines()

def send(data, unsorted, elapsed, startdate, enddate, lucky_numbers):
    days = int(elapsed.days)
    hours = int(elapsed.seconds/(60**2)%24)
    minutes = int(elapsed.seconds/(60)%60)
    seconds = int(elapsed.seconds%60)
    msg = EmailMessage()
    msg['Subject'] = f'Bogosortbot has finished sorting a {len(data)} number data set [{days}:{hours}:{minutes}:{seconds}]'
    msg.set_content(f"""
    Unsorted Data Set:  {unsorted}
    Sorted Data Set:     {data}
    Data Set Length:     {len(data)} numbers
    Bogosortbot's Work Time:
        {days} days,
        {hours} hours,
        {minutes} minutes,
        {seconds} seconds
        Started on  {startdate}
        Finished on {enddate}
    Thank you for being one of Bogosortbot's {len(fans)} fans!
    Today's lucky numbers:
        {lucky_numbers}
    """)


    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(creds.username,creds.password)
    server.sendmail(creds.username, fans, str(msg))
    server.quit()
