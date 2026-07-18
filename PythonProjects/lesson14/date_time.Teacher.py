import datetime

# from datetime import date,timedelta
# now = datetime.datetime.now()
# print(now)

# today = datetime.date.today()
# print(today)

# todays = datetime.date.today()
# print(todays.year)
# print(todays.month)
# print(todays.day)


# today = datetime.date.today()
# format = today.strftime("%Y/%m/%d")
# other = today.strftime("%y/%m/%d")
# others = today.strftime("%d:%m:%Y")
# print(format)
# print(other)
# print(others)

# You are given several examples of how a date should be displayed. 
# Your task is to write Python code using the datetime module and the 
# .strftime() method to produce exactly the same output format.
# Example outputs to reproduce:
# 30/07/2025
# 07-30-2025
# Wednesday, July 30, 2025
# Wed, Jul 30
# 2025-07-30
# The output of will depend on the current date when you run the program. 
# The examples shown are just sample outputs.

# today = datetime.date.today()
# format = today.strftime("%d:%m:%Y")
# format1 = today.strftime("%m-%d-%Y")
# format2 = today.strftime("%A, %B %d, %Y")
# format3 = today.strftime("%a, %b %d")
# format4 = today.strftime("%Y-%m-%d")
# print(format)
# print(format1)
# print(format2)
# print(format3)
# print(format4)

forma = input("enter a date: ")
# print(type(forma))
converts = datetime.datetime.strptime(forma,"%d-%m-%Y")
print(type(converts))

only_date = converts.date()
print(only_date)

# You are given several strings that represent dates in different formats. 
# Your task is to write Python code using the datetime module and the 
# .strptime() method to convert each string into a valid datetime object.
# Strings to parse:


# first = "30/07/2025"
# second = "Jul 30, 2025"
# Thirty= "Wednesday, July 30 2025"
# last = "30-Jul-25"
# last_one = "20250730"


# covert_first = datetime.datetime.strptime(first, "%d/%m/%Y")
# print(type(covert_first))
# cut = covert_first.date()
# print(cut)
# convert_2 = datetime.datetime.strptime(second , "%b %d, %Y")
# print(convert_2)
# convert_s3 = datetime.datetime.strptime(Thirty, "%A, %B %d %Y")
# print(convert_s3)
# convert_s4 = datetime.datetime.strptime(last, "%d-%b-%y")
# convert_s5 = datetime.datetime.strptime(last_one, "%Y%m%d")
# print(convert_s4)
# print(convert_s5)

# today = datetime.date.today()
# delta = today + datetime.timedelta(days = 7)
# print(delta)

# today = datetime.date.today()
# delta = today - datetime.timedelta(days = 7)
# print(delta)

# start = datetime.date(2025,10,14)
# end = datetime.date(2025,5,14)
# delta = end - start
# print(delta)

# today = datetime.datetime.now()
# later = today + datetime.timedelta(hours = 2, minutes = 30)
# print(later)

# deadline = datetime.datetime(2025,5,16,15,0)
# extesion = datetime.timedelta(hours = 2,minutes = 55)
# new_deadline = deadline + extesion
# print(new_deadline)

# from datetime import time, timedelta  
    
# A = timedelta(minutes = 55)

# totalsecond = A.total_seconds()

# # print("Total seconds in 55 minutes:", totalsecond)

# # A = datetime.timedelta(minutes = 55)

# # totalsecond = A.total_seconds()
# # print("Total seconds in 55 minutes:", totalsecond)


# # Find the date that is exactly 10 days from today.
# # Instructions:
# # Use datetime.date.today() to get the current date.
# # Use timedelta(days=10) to calculate the future date.
# # Print the result.
# # Expected output: A date 10 days ahead of the current day (e.g., 2025-08-09 if today is 2025-07-30).
# today = datetime.date.today()
# later = today + datetime.timedelta(days=10)
# print("A date 10 days ahead of the current day", later)


# # Calculate the date that was 3 weeks before today.
# # Instructions:
# # Use datetime.date.today() to get the current date.
# # Use timedelta(weeks=3) and subtract it.
# # Print the resulting date.
# # Expected output: A past date, 21 days before today.
# weeks = datetime.date.today()
# before = weeks - datetime.timedelta(weeks= 3)
# print(before)


# # You have a deadline on 15 December 2025. Calculate how many days are left from today.
# # Instructions:
# # Create a date object for the deadline.
# # Use datetime.date.today() for today’s date.
# # Subtract the two and print the number of days.
# # Expected output: A positive number showing remaining days.
# # deadline = datetime(2025,12,15)
# # today = datetime.today()
# # how_much = deadline - today
# # print(how_much)
# # today = datetime.date.today()
# # deadline = datetime.date(2025, 12, 15)
# # days = deadline - today
# # print(days)


# # An event starts today at 14:00 (2 PM) and lasts for 5 hours and 45 minutes. Find the end time.
# # Instructions:
# # Create a datetime object with today’s date and time 14:00.
# # Use timedelta(hours=5, minutes=45).
# # Add it and print the result.
# # Expected output: A datetime object showing the event’s end time.
# eventStart = datetime.datetime(2025, 10, 12, 14)
# event = datetime.timedelta(hours = 5, minutes = 45)
# eventStop = eventStart + event 
# print(eventStop)