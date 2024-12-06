import os

from email.mime.text import MIMEText
# for encoding/decoding messages in base64
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



SCOPES = ["https://mail.google.com/"]

# Authenticates the user and creates client service for api use
def gmail_authenticate():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())
    try:
        service = build("gmail", "v1", credentials=creds)
    except HttpError as error:
        print(f"An error has ocurred: {error}")
    return service

# Get message ids of all unread messages with a query
def get_unread_tips_emails_ids(service, query):
    try:
        result = service.users().messages().list(userId="me", q=query).execute()
    except HttpError as error:
        print(f"An error has ocurred: {error}")
    messages = []
    message_ids = []
    if "messages" in result:
        messages.extend(result["messages"])
    for i in range(len(messages)):
        message_ids.append(messages[i]["id"])
    if not message_ids:
        print("No new messages")
    return message_ids

# Gets the snippet info for message.  It's basically the whole body of the message as 
# we don't have a message that's longer than what the snippet returns.
def get_message_snippet(service, message_id):
    if message_id:
            try:
                result = service.users().messages().get(userId="me", id=message_id).execute()
                snippet = result["snippet"]
            except HttpError as error:
                print(f"An error has ocurred: {error}")
    else:
        print("No new messages")
    return snippet

# Get the date header value of a message and returns the value
def get_date(service, message_id):
    message_part = service.users().messages().get(userId="me", id=message_id).execute()
    payload = message_part["payload"]
    headers = payload["headers"]
    for header in headers:
        if header["name"] == "Date":
            date = header["value"]
    return date

# Takes a list of message ids and removes the UNREAD label from all of the messages
def mark_as_read(service, message_ids):
    try:
        service.users().messages().batchModify(
            userId="me", body={"ids": message_ids, "removeLabelIds": ["UNREAD"]}
        ).execute()
    except HttpError as error:
        print(f"An error has ocurred: {error}")

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
    return {
        'raw': raw_message.decode('utf-8')
    }

def send_message(service, user_id, message):
  try:
    message = service.users().messages().send(userId=user_id, body=message).execute()
    print('Message Id: %s' % message['id'])
    return message
  except Exception as e:
    print('An error occurred: %s' % e)
    return None