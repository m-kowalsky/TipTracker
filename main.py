from get_dates import get_day
from user_prompts import hours_prompt, make_dir, tip_prompts, write_to_file


def main():
        
    day = get_day()
    make_dir()

    hours = hours_prompt()
    tips = tip_prompts()
    write_to_file(hours, tips, day)


main()
