from gmail_api import (
    get_unread_tips_emails_ids,
    gmail_authenticate,
    # mark_as_read,
    
)
from parse_message_data import make_message_dict
from generate_report import get_daily_tips_and_hours


def main():

    service = gmail_authenticate()
    message_ids = get_unread_tips_emails_ids(service, "subject: tips label:unread")
    message_data = make_message_dict(service, message_ids)
    dollar_formatted_tips, tips, hours = get_daily_tips_and_hours(message_data)
    

main()
