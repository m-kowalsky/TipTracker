import os

dir_path = "Desktop/Tips"


def get_tips_and_hours(message_dict):
    total_hours = 0
    total_tips = 0
    for id in message_dict:
        total_hours += message_dict[id]["snippet"]["hours"]
        total_tips += message_dict[id]["snippet"]["tips"]
    formatted_tips = f"${total_tips:.2f}"

    return formatted_tips, total_hours


def daily_tips_report_to_append_to_file(message_id, tips, hours):
    date = message_id["date"]
    template_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/PersonalProject1/Day tip template"
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    template = template.replace("<date>", date)
    template = template.replace("<hours>", hours)
    template = template.replace("<tips>", tips)
    return template
    


def get_month(date):
    date_list = date.split()
    month = date_list[2]
    return month
