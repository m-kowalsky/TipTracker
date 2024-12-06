import json
import os


def get_daily_tips_and_hours(message_dict, message_id):

    hours = message_dict[message_id]["snippet"]["hours"]
    tips = message_dict[message_id]["snippet"]["tips"]

    return hours, tips


def write_tips_hours_to_json(tips, hours, date):
    month = get_month(date)
    year = get_year(date)

    # Create json file if data.json doesn't exist yet
    if not os.path.exists("data.json"):
        data = {
            year: {
                month: {"tips": 0.0, "hours": 0.0},
            },
        }
        print("Creating data.json file")
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
    # Open json file and load to data
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
        print(f"data.json file: {data}")
    # Create new year and month if not in data.json
    if year not in data:
        data[year] = {month: {"tips": 0, "hours": 0}}
    if month not in data[year]:
        data[year][month] = {"tips": 0, "hours": 0}
    data[year][month]["tips"] += tips
    data[year][month]["hours"] += hours

    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def daily_tips_report_to_append_to_file(tips, hours, date):
    year = get_year(date)
    month = get_month(date)
    template_path = "/Users/michaelkowalsky/workspace/github.com/KarlHavoc/PersonalProject1/Day tip template"
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    template = template.replace("<date>", date)
    template = template.replace("<daily hours>", str(hours))
    template = template.replace("<daily tips>", str(tips))
    # replace <total_hours> and <total_tips> with data from json data file
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    total_hours = round(data[year][month]["hours"], 2)
    total_tips = round(data[year][month]["tips"], 2)
    template = template.replace("<total hours>", str(total_hours))
    template = template.replace("<total tips>", str(total_tips))
    template = template.replace("<month>", month)

    return template


def append_template_to_monthly_tip_file(template_to_append, date):
    month = get_month(date)
    desktop_path = os.path.expanduser("~/Desktop")
    # take the template to append and write it to the Month/Tips.txt file
    main_dir_path = os.path.join(desktop_path, "Tips")
    tips_file_dir = os.path.join(main_dir_path, month)
    file_path = os.path.join(tips_file_dir, "Tips.txt")
    if not os.path.exists(main_dir_path):
        os.mkdir(main_dir_path)
    if not os.path.exists(tips_file_dir):
        os.mkdir(tips_file_dir)
    with open(file_path, "a+") as tips_file:
        tips_file.write(template_to_append)


def get_month(date):
    date_list = date.split()
    month = date_list[2]
    return month


def get_year(date):
    date_list = date.split()
    year = date_list[3]
    return year
