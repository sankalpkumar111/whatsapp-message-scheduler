from twilio.rest import Client
from datetime import datetime,timedelta
import time
import dotenv
dotenv.load_dotenv()
import os

# Your Account SID from twilio.com/console

account_sid=os.getenv('ACCOUNT_SID')
auth_token=os.getenv('AUTH_TOKEN')

client=Client(account_sid,auth_token)

# Send message functionq

def send_whatsapp_message(recipient_number,message_body):
    try:
        message=client.messages.create(
            from_=os.getenv('TWILIO_NO'),
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! message sid: {message.sid}')
    except Exception as e:
        print(f'Error sending message: {e}')
    
    
# user input:
name=input('Enter the recipient name: ')
recipient_number=input('Enter the recipient whatsapp number with country code(eg: +91): ')
message_body=input(f'Enter the message you want to send to {name}')

# parse datetime and calculate time difference

date_str=input('Enter the date to send message(yyyy-mm-dd): ')
time_str=input('Enter the time to send the message(HH:MM in 24 hour format): ')
date_time_str=f'{date_str} {time_str}'

date_time_obj=datetime.strptime(date_time_str,'%Y-%m-%d %H:%M')

current_datetime=datetime.now()
time_difference=date_time_obj-current_datetime

delay_in_seconds=time_difference.total_seconds()

if delay_in_seconds<=0:
     print("The specified time is in the past.Please Enter a future date and time.")
else:
     print(f'Message scheduled to be sent to {name} at {date_time_str}')
    #  Wait until the scheduled time
     time.sleep(delay_in_seconds)
    #  Send the message
     send_whatsapp_message(recipient_number,message_body)
     
            
