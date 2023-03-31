# TOOLS FOR DATE AND TIME CALCULATIONS

# LIBRARIES AND MODULES
import datetime

def date_diff(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2-d1).days)

def time_diff(t1, t2):
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    second = abs((t2-t1).seconds)
    hours = second / 3600
    return hours

def date_diff_2(d1, d2, unit: str):
    units = {'day': 1, 'year': 365, 'month': 30}
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2-d1).days)
    divider = units.get(unit, 1)
    value = difference / divider
    return value

def time_diff_2(t1, t2, unit:str):
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    second = abs((t2-t1).seconds)
    units = {'hour': 3600, 'minute': 60, 'second': 1}
    divider = units.get(unit, 1)
    value = second / divider
    return value

if __name__=='__main__':

    date1 = '2023-03-21'
    date2 = '2023-03-17'
    ero = date_diff_2(date1, date2, 'day')
    print('ero oli', ero, 'päivää')

    time1 = '10:00:00'
    time2 = '15:25:00'
    ero = time_diff_2(time1, time2, 'minute')
    print('Aikaero oli', ero, 'minuuttia')