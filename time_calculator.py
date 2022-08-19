# Calculates time of arrival (in 12-hour format) based on time of departure and duration.
# A day of the week is accepted as an optional argument.

def add_time(start_time, duration, start_day=None):
    start_time_sp = start_time.split()[0]
    am_pm = start_time.split()[1]
    hour = int(start_time_sp.split(":")[0])
    minute = int(start_time_sp.split(":")[1])
    dur_hour = int(duration.split(":")[0])
    dur_minute = int(duration.split(":")[1])
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    n = 0

    if hour == 12 and am_pm == "AM":
        hour = 0
    elif hour < 12 and am_pm == "PM":
        hour = hour + 12

    am_pm = ""
    end_minute = minute + dur_minute
    if end_minute >= 60:
        end_minute = end_minute - 60
        hour = hour + 1

    if dur_hour >= 24:
        d = int(dur_hour / 24)
        n = n + d
        dur_hour = dur_hour - 24 * n

    end_hour = hour + dur_hour
    if end_hour >= 24:
        end_hour = end_hour - 24
        n = n + 1

    if 0 < end_hour <= 11:
        am_pm = "AM"
    elif end_hour == 0:
        am_pm = "AM"
        end_hour = 12
    elif end_hour == 12:
        am_pm = "PM"
    elif end_hour > 12:
        am_pm = "PM"
        end_hour = end_hour - 12

    str_end_hour = str(end_hour)
    str_end_minute = ""
    if end_minute < 10:
        str_end_minute = "0" + str(end_minute)
    elif end_minute >= 10:
        str_end_minute = str(end_minute)
    new_time = ""
    if start_day is None:
        if n == 0:
            new_time = str_end_hour + ":" + str_end_minute + " " + am_pm
        elif n == 1:
            new_time = str_end_hour + ":" + str_end_minute + " " + am_pm + " (next day)"
        elif n > 1:
            new_time = str_end_hour + ":" + str_end_minute + " " + am_pm + " (" + str(n) + " days later)"
    elif start_day.lower() in days:
        m = days.index(start_day.lower())
        m = m + n % 7
        if m > 6:
            m = m - 7
        end_day = days[m].capitalize()
        if n == 0:
            new_time = str_end_hour + ":" + str_end_minute + " " + am_pm + ", " + end_day
        elif n == 1:
            new_time = str_end_hour + ":" + str_end_minute + " " + am_pm + ", " + end_day + " (next day)"
        elif n > 1:
            new_time = str_end_hour + ":" + str_end_minute + " " + am_pm + ", " \
                       + end_day + " (" + str(n) + " days later)"

    return new_time
