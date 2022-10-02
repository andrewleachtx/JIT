from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime, time, timezone, timedelta


def utc_to_cst(utc_dt):
    cstTimeDelta = timedelta(hours=-5)
    cstTZObject = timezone(cstTimeDelta, name="CST")
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=cstTZObject)

class myCal:
    def __init__(self, name, location, startTime, endTime, days):
        self.name = name
        self.location = location
        self.startTime = utc_to_cst(startTime).time()
        self.endTime = utc_to_cst(endTime).time()
        self.days = days
    
    def __str__(self):
        return f"{self.name}\n{self.location}\n{self.startTime}\n{self.endTime}\n{self.days}"

classes = []

# code to convert ics to list of Class objets
def icsConvert(scheduleFile):
    s = open(scheduleFile,'rb')
    schedule = Calendar.from_ical(s.read())
    for component in schedule.walk():
        if component.name == "VEVENT":
            key = list(component.get("rrule").keys())[-1]
            classes.append(Class(component.get("summary"), component.get("location"), component.decoded("dtstart"), component.decoded("dtend"), component.get("rrule")[key]))
    s.close()
    
    return classes