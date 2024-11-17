import os

from get_dates import get_day, get_month

day = get_day()
month = get_month()

folder_path = "/Users/michaelkowalsky/Desktop/" + month + "_Tips"
complete_file_path = os.path.join(folder_path, month + "_tips" + ".txt")


def make_dir():
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    return

def tip_prompts():
    name = input("What is your name? ")


    file1 = open(complete_file_path, "a")

    file1.write(day + "\n")
    file1.write(name + "\n\n\n")
    file1.close()   