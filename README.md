# Twilio WhatsApp Message Scheduler

A Python script that allows you to schedule WhatsApp messages to be sent using the Twilio API. The script takes user input for the recipient's number, message content, and the scheduled time, then sends the message at the specified time.

## Features
- Schedule WhatsApp messages to be sent at a future date and time.
- Send messages via the Twilio API.
- Load sensitive credentials (like Twilio API keys) securely from a `.env` file.
- Simple and easy-to-use interface.

## Requirements

- Python 3.x
- A Twilio account with a WhatsApp-enabled phone number.
- Python libraries:
  - `twilio` (for integrating Twilio)
  - `python-dotenv` (for securely loading environment variables)

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/yourusername/twilio-whatsapp-scheduler.git
cd twilio-whatsapp-scheduler
```

### 2. Install Dependencies

Make sure you have Python 3.x installed. Then, install the required Python libraries:

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, you can create one using:

```bash
pip freeze > requirements.txt
```

The required libraries are:
- `twilio` – for sending WhatsApp messages via the Twilio API.
- `python-dotenv` – to securely load environment variables from a `.env` file.

### 3. Set Up Environment Variables

Create a `.env` file in the project root directory and add the following Twilio credentials:

```plaintext
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_NO=whatsapp:+your_twilio_whatsapp_number
```

You can find your Twilio credentials by logging into your [Twilio Console](https://www.twilio.com/console).

### 4. Run the Script

After setting up the environment variables, you can run the script:

```bash
python message_scheduler.py
```

The script will ask you for the following information:
- The recipient's name.
- The recipient's WhatsApp number (with country code).
- The message you want to send.
- The date and time when you want the message to be sent.

It will then calculate the time delay and send the message when the scheduled time arrives.

## Example Usage

The script will prompt you for the following inputs:

```
Enter the recipient name: John
Enter the recipient whatsapp number with country code(eg: +91): +1234567890
Enter the message you want to send to John: Hello John, this is a scheduled message!
Enter the date to send message(yyyy-mm-dd): 2025-02-20
Enter the time to send the message(HH:MM in 24 hour format): 14:30
```

After confirming the inputs, the script will calculate the delay and wait until the specified time before sending the message via WhatsApp.

## .gitignore

The `.gitignore` file ensures that sensitive information (like `.env`) is not tracked by Git. The following files are ignored:
- `.env`
- Python bytecode files (`*.pyc`)
- IDE-specific files and directories (`.vscode/`, `.idea/`)

## Troubleshooting

- **Authentication Error (20003)**: Ensure your Twilio credentials (`ACCOUNT_SID` and `AUTH_TOKEN`) are correct and stored in the `.env` file.
- **Time not scheduled correctly**: Ensure that you provide the time in the correct 24-hour format (e.g., `14:30` for 2:30 PM).
- **Message not sent**: If the message fails to send, check your internet connection and Twilio account status.


