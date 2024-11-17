from get_dates import get_day, get_month
from user_prompts import make_dir, tip_prompts


def main():

    month = get_month()
    day = get_day()
    print(month)
    print(day)
    make_dir()
    tip_prompts()


main()
