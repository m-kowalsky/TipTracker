from gmail_api import get_date, get_message_snippet
import re
 
def make_message_dict(service, message_ids):
    message_dict = {}
    for id in message_ids:
        date = get_date(service, id)
        snippet = get_message_snippet(service, id)
        message_dict[id] = {"date": date, "snippet": snippet}
    return message_dict

def parse_snippet(snippet):
    hours = re.search('@(.*)@', snippet)
    tips = re.search('#(.*)#', snippet)
    return hours, tips

