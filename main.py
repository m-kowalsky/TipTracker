from gmail_api import (
    get_unread_tips_emails_ids,
    gmail_authenticate,
    # mark_as_read,
    
)
from parse_message_data import make_message_dict
from generate_report import get_tips_and_hours


def main():

    service = gmail_authenticate()
    message_ids = get_unread_tips_emails_ids(service, "subject: tips label:unread")
    message_data = make_message_dict(service, message_ids)
    # print(message_data)
    # for key in message_data:
    #     print(type(message_data[key]["date"]))

    # message_part = service.users().messages().get(userId="me", id=message_ids[0]).execute()
    # payload = message_part["payload"]
    # headers = payload["headers"]
    # print(headers)

    # mark_as_read(service, message_ids)
    tips, hours = get_tips_and_hours(message_data)
    print(f"tips: {tips}\nhours: {hours}")

main()
