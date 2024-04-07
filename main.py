from datetime import datetime
from datetime import date
import math

#total course count as of 02/14/24
total_courses = 1251

#Completed problems as of 02/15/24
problems_completed = 353


#Function to calculate incomplete assignments
def get_incomplete_courses(completed):
    return total_courses - completed

incomplete = get_incomplete_courses(problems_completed)


end_date = {
      "Month": 12,
      "Day": 1,
      "Year": 2024,
      "FullDate": date(2024,12,1),
}


print(f"Remaining Assignments: {incomplete}")

#Stores today date in instanced object
today_date = datetime.today()

year = today_date.year
month = today_date.month
day = today_date.day
todays_date = date(year, month, day)


def get_days_left():
    difference_in_days = (end_date["FullDate"] - todays_date).days
    #print(f"Difference in Days: {difference_in_days}")
    return difference_in_days

days_left = get_days_left()

def get_avg_assignments(days):
    avg = (incomplete) / days
    print(f"Average Assignments to complete a day: {math.ceil(avg)}")
    print(f"Not rounded: {(avg)}")
    return avg

get_avg_assignments(days_left)