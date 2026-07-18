import datetime
# today = datetime.date.today()
# print(today)
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)

# format = today.strftime("%d/%m/%Y")
# print("Formatted date:", format)

# You are given several strings that represent dates in different formats. Your task is to write Python code using the datetime module and the .strptime() method to convert each string into a valid datetime object.
# Strings to parse:
# "30/07/2025"
# "Jul 30, 2025"
# "Wednesday, July 30 2025"
# "30-Jul-25"
# "20250730
# import datetime

# s1 = "30/07/2025"
# s2 = "Jul 30, 2025"
# s3 = "Wednesday, July 30 2025"
# s4 = "30-Jul-25"
# s5 = "20250730"

# convert_s1 = datetime.datetime.strptime(s1, "%d/%m/%Y")
# convert_s2 = datetime.datetime.strptime(s2, "%b %d, %Y")
# convert_s3 = datetime.datetime.strptime(s3, "%A, %B %d %Y")
# convert_s4 = datetime.datetime.strptime(s4, "%d-%b-%y")
# convert_s5 = datetime.datetime.strptime(s5, "%Y%m%d")

# print(convert_s1)
# print(convert_s2)
# print(convert_s3)
# print(convert_s4)
# print(convert_s5)

# today = datetime.date.today()
# delta = today + datetime.timedelta(days=7) # calc astazi + 7 zile
# print(delta)

# today = datetime.date.today()
# delta = today - datetime.timedelta(days=7) # calc astazi - 7 zile
# print(delta)

# start = datetime.date(2025, 7, 1)
# end = datetime.date(2025, 7, 30)
# delta = end - start
# print("Days between:", delta.days)

# now = datetime.datetime.now()
# later = now + datetime.timedelta(hours=2, minutes=30) # adds 2,5h to the current time
# print("After 2 hours and 30 minutes:", later)

# deadline = datetime.datetime(2025, 7, 30, 15, 0) # year, month, day, hour, minute
# extension = datetime.timedelta(days=2, hours=4)
# new_deadline = deadline + extension
# print("New deadline:", new_deadline)

# from datetime import time, timedelta
# A = timedelta(minutes=55)
# total_seconds = A.total_seconds()
# print("Total seconds in 55 minutes:", total_seconds)

# Task 1
# now = datetime.datetime.now()
# ago = now - datetime.timedelta(weeks=3)
# print("Date 3 weeks ago:", ago)

#Task 2
# start = datetime.date.today()
# end = datetime.date(2025, 12, 15)
# delta = end - start
# print("Days until 15 Dec 2025:", delta.days)

# Task 3
# meeting_time = datetime.datetime(2025, 10, 20, 14, 0)
# last = meeting_time + datetime.timedelta(hours=5, minutes=45)
# print("Meeting ends at:", last)

