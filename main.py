# from get_dates import get_day
# from user_prompts import hours_prompt, make_dir, tip_prompts, write_to_file
from gmail_api import (
    get_message_snippet,
    get_unread_tips_emails_ids,
    gmail_authenticate,
    mark_as_read,
)


def main():
    # Get todays date
    # day = get_day()

    # Make directory for tips folder on desktop if there isn't one
    # make_dir()

    # Prompt user for hours and tips and then right that to a file in tips folder on desktop
    # hours = hours_prompt()
    # tips = tip_prompts()
    # write_to_file(hours, tips, day)

    service = gmail_authenticate()
    message_ids = get_unread_tips_emails_ids(service, "label:tips label:unread")
    if not message_ids:
        print("No new messages")
        return
    snippets = get_message_snippet(service, message_ids)
    print(snippets)
    mark_as_read(service, message_ids)


main()
