import json
import os


def get_daily_tips_and_hours(message_dict):
    total_hours = 0
    total_tips = 0
    for id in message_dict:
        total_hours += message_dict[id]["snippet"]["hours"]
        total_tips += message_dict[id]["snippet"]["tips"]
    dollar_formatted_tips = f"${total_tips:.2f}"

    return dollar_formatted_tips, total_tips, total_hours


def write_tips_hours_to_json(tips, hours, date):
    month = get_month(date)
    year = get_year(date)

    # Create json file if data.json doesn't exist yet
    if not os.path.exists("data.json"):
        data = {
            year: {
                month: {"tips": tips, "hours": hours},
            },
        }
        with open("data.json", "w+") as json_file:
            json.dump(data, json_file)
    # Open json file and load to data
    with open("data.json", "r+") as json_file:
        data = json.load(json_file)
    # Create new year and month if not in data.json
    if year not in data:
        data[year] = {month: {"tips": tips, "hours": hours}}
    if month not in data[year]:
        data[year][month] = {"tips": tips, "hours": hours}
    else:
        data[year][month]["hours"] += hours
        data[year][month]["tips"] += tips

    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def daily_tips_report_to_append_to_file(message_id, tips, hours):
    date = message_id["date"]
    template_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/PersonalProject1/Day tip template"
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    template = template.replace("<date>", date)
    template = template.replace("<daily hours>", hours)
    template = template.replace("<daily tips>", tips)
    # replace <total_hours> and <total_tips> with data from json data file
    ...


def write_template_to_monthly_tip_file(template_to_append, month):
    # take the template to append and write it to the Month/Tips.txt file
    dir_path = "~/Desktop/Tips"
    file_path = os.path.join(dir_path, month, "Tips.txt")
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    monthly_tips_file = open(file_path, "r+")
    monthly_tips_file.close()

    ...


def get_month(date):
    date_list = date.split()
    month = date_list[2]
    return month


def get_year(date):
    date_list = date.split()
    year = date_list[3]
    return year


date = "Wed, 27 Nov 2024"
write_tips_hours_to_json(123.45, 4.5, date)
