days_to_nums = {
    "Sunday" : 1,
    "Monday" : 2,
    "Tuesday" : 3,
    "Wednesday" : 4,
    "Thursday" : 5,
    "Friday" : 6,
    "Saturday" : 7
}

nums_to_days = {
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday"
}

def str_to_int(strings):
    for i in range(0, len(strings)):
        strings[i] = int(strings[i])

    return strings        


def add_time(start, duration, day_of_week = ""):
    start_hr, start_min, start_period = start.replace(":", " ").split()
    duration_hr, duration_min = duration.split(":")
    day_of_week = day_of_week.lower().capitalize()
    
    start_hr, start_min, duration_hr, duration_min = str_to_int([start_hr, start_min, duration_hr, duration_min])

    if start_period == "PM":
        start_hr += 12

    new_min = start_min + duration_min
    new_hr = (int)((new_min / 60) + duration_hr + start_hr)
    days_later = (int)(new_hr / 24)
    new_min = new_min % 60
    new_hr = new_hr % 24

    new_period = "AM"
    if new_hr >= 12:
        new_period = "PM"
    if new_hr > 12:
        new_hr -= 12
    if new_hr == 0:
        new_hr += 12

    days_later_str = ""
    if days_later == 1:
        days_later_str += " (next day)"
    elif days_later > 1:
        days_later_str += " (" + str(days_later) + " days later)"

    new_day_of_week = ""
    if day_of_week != "":
        new_day_of_week += ", " + nums_to_days[(days_to_nums[day_of_week] + days_later)%7]
    
    return str(new_hr) + ":" + str(new_min).zfill(2) + " " + new_period + new_day_of_week + days_later_str