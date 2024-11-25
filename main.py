from gmail_api import (
    # get_message_snippet,
    get_unread_tips_emails_ids,
    gmail_authenticate,
    # mark_as_read,
)
from parse_message_data import make_message_dict


def main():
    

    service = gmail_authenticate()
    message_ids = get_unread_tips_emails_ids(service, "subject: tips label:unread")
    message_data = make_message_dict(service, message_ids)
    print(message_data)
    for key, value in message_data.items():
        print(f"key: {key}")
        print(f"value: {value}")
        print(f"date: {value["date"]}")
        
        
    # mark_as_read(service, message_ids)


main()
