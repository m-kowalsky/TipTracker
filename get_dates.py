from datetime import datetime


def get_day():
    now = datetime.now()
    today = now.strftime("%Y/%m/%d")

    return today

def get_month():
    now = datetime.now()
    month = now.strftime("%B")
    return month

