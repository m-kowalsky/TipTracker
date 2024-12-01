import os
import json

def get_daily_tips_and_hours(message_dict):
    total_hours = 0
    total_tips = 0
    for id in message_dict:
        total_hours += message_dict[id]["snippet"]["hours"]
        total_tips += message_dict[id]["snippet"]["tips"]
    dollar_formatted_tips = f"${total_tips:.2f}"

    return dollar_formatted_tips, total_tips, total_hours

def tips_hours_to_json(tips, hours, month):
    # Initial data dump if data.json doesn't exist yet
    if not os.path.exists("data.json"):
        data = {
            month: {
            "tips": tips, 
            "hours": hours
            }
        }
        with open("data.json", "w+") as json_file:
            json.dump(data, json_file)
    with open("data.json", "r+") as json_file:
        data = json.load(json_file)
    
    data[month]["hours"] += hours
    data[month]["tips"] += tips

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
    #replace <total_hours> and <total_tips> with data from json data file
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

tips_hours_to_json(123.45, 4.5, "Nov")
