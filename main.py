#total course count as of 02/14/24
total_courses = 1226

#Completed problems as of 02/14/24
problems_completed = 308

#Function to calculate incomplete assignments owo
def get_incomplete_courses(completed):
    incomplete = total_courses - completed
    return incomplete

print(f"Total Assignments: {total_courses}")
print(f"Assignments Completed: {problems_completed}")
print(f"Remaining Assignments: {get_incomplete_courses(problems_completed)}")