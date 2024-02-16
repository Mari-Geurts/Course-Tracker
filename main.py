from datetime import datetime
from datetime import date
import math

#total course count as of 02/14/24
total_courses = 1226

#Completed problems as of 02/15/24
problems_completed = 318

#Function to calculate incomplete assignments
def get_incomplete_courses(completed):
    return total_courses - completed


joined_date = {
      "Month": 12,
      "Day": 1,
      "Year": 2023,
      "FullDate": date(2023,12,1),
}

end_date = {
      "Month": 12,
      "Day": 1,
      "Year": 2024,
      "FullDate": date(2024,12,1),
}


#print(f"Total Assignments: {total_courses}")
#print(f"Assignments Completed: {problems_completed}")
print(f"Remaining Assignments: {get_incomplete_courses(problems_completed)}")

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

def get_avg_assignments(difference):
    avg = (get_incomplete_courses(problems_completed)) / difference
    print(f"Average Assignments to complete a day: {math.ceil(avg)}")
    return avg

get_avg_assignments(get_days_left())