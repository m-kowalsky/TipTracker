import os

from get_dates import get_day, get_month

day = get_day()
month = get_month()

folder_path = "/Users/michaelkowalsky/Desktop/" + "Tips" + month
complete_file_path = os.path.join(folder_path, month + "_tips" + ".txt")


def make_dir():
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    return


def hours_prompt():
    hours = input("How many hours did you work today? ")
    hours_correct = input(
        "You entered " + hours + " hours for " + day + ".  Is this correct? y/n "
    )
    hours_correct = hours_correct.lower()
    if hours_correct == "y":
        return hours
    else:
        hours_prompt()


def tip_prompts():
    tips = input("How much money did you make today? ")
    tips_correct = input(
        "You entered $" + tips + " for " + day + ".  Is this correct? y/n "
    )
    tips_correct = tips_correct.lower()
    if tips_correct == "y":
        return tips
    else:
        tip_prompts()


def write_to_file(hours, tips, month, day):
    file1 = open(complete_file_path, "a")

    file1.write(day + "\n")
    file1.write("Hours worked: " + str(hours) + "\n")
    file1.write("Tips made: " + str(tips) + "\n")
    file1.write("Tips per hour: " + str(float(tips) / float(hours)))
    file1.close()
    print(f"Text file updated and saved to {complete_file_path}")
