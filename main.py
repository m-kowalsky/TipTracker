from gmail_api import (
    get_unread_tips_emails_ids,
    gmail_authenticate,
    # mark_as_read,
    
)
from parse_message_data import make_message_dict, get_date
from generate_report import get_daily_tips_and_hours, write_tips_hours_to_json, daily_tips_report_to_append_to_file, append_template_to_monthly_tip_file


def main():
    # Create gmail client service
    service = gmail_authenticate()
    # Get email message ids for unread emails with 'tips' in subject line
    message_ids = get_unread_tips_emails_ids(service, "subject: tips label:unread")
    # Make a dict of all the messages and parse message for tips and hours data
    message_data = make_message_dict(service, message_ids)
    # Loop through message data by id
    for id in message_data:
        # get date
        date = get_date(service, id)
        # get daily tips and hours
        tips_to_dollars, daily_hours, tips = get_daily_tips_and_hours(message_data, id)
        # write tips and hours to json data file
        write_tips_hours_to_json(tips, daily_hours, date)
        # report to tip template
        template = daily_tips_report_to_append_to_file(id, tips_to_dollars, daily_hours, date)
        # append template to tips file
        append_template_to_monthly_tip_file(template, date)
        

main()
