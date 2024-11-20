from get_dates import get_day, get_month
from user_prompts import hours_prompt, make_dir, tip_prompts, write_to_file


def main():

    month = get_month()
    day = get_day()
    make_dir()

    hours = hours_prompt()
    tips = tip_prompts()
    write_to_file(hours, tips, month, day)

main()
