from gmail_api import get_date, get_message_snippet

"""Takes gmail client service and list of message ids and formats it into a nested dictionary
    {"id":
        {
        "date": date,
        "snippet": {
            "hours": hours,
            "tips": tips
            },
        }
    }
"""


def make_message_dict(service, message_ids):
    message_dict = {}
    for id in message_ids:
        date = get_date(service, id)
        snippet = get_message_snippet(service, id)
        message_dict[id] = {"date": date, "snippet": snippet_to_dict(snippet)}
    return message_dict


# Converts snippet string to json and return error if string is formatted incorrectly
def snippet_to_dict(snippet):
    snippet = snippet.split()
    data = {}
    for i in range(len(snippet)):
        if snippet[i] == "Hours" or snippet[i] == "hours":
            data[snippet[i].lower()] = round(float(snippet[i + 1]), 2)
        if snippet[i] == "Tips" or snippet[i] == "tips":
            data[snippet[i].lower()] = round(float(snippet[i + 1]), 2)
    return data
