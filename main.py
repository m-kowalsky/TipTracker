from gmail_api import (
    # get_message_snippet,
    get_unread_tips_emails_ids,
    gmail_authenticate,
    # mark_as_read,
)


def main():
    

    service = gmail_authenticate()
    message_ids = get_unread_tips_emails_ids(service, "subject: tnt tips label:unread")
    
   
    
        
        
    # mark_as_read(service, message_ids)


main()
