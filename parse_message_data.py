from gmail_api import get_date, get_message_snippet


def make_message_dict(service, message_ids):
    message_dict = {}
    for id in message_ids:
        date = get_date(service, id)
        snippet = get_message_snippet(service, id)
        message_dict[id] = {"date": date, "snippet": snippet}
