import os

# for encoding/decoding messages in base64
# from base64 import urlsafe_b64decode
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# for dealing with attachement MIME types
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# from email.mime.audio import MIMEAudio
# from email.mime.base import MIMEBase
# from mimetypes import guess_type as guess_mime_type

SCOPES = ["https://mail.google.com/"]


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
    return message_ids


def get_message_snippet(service, message_ids):
    snippets = []
    if message_ids:

        for id in message_ids:
            try:
                result = service.users().messages().get(userId="me", id=id).execute()
                snippet = result["snippet"]
                snippets.append(snippet)
            except HttpError as error:
                print(f"An error has ocurred: {error}")
    else:
        print("No new messages")
    return snippets


def mark_as_read(service, message_ids):
    try:
        service.users().messages().batchModify(
            userId="me", body={"ids": message_ids, "removeLabelIds": ["UNREAD"]}
        ).execute()
    except HttpError as error:
        print(f"An error has ocurred: {error}")
