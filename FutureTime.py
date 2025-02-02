#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) 
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = int(input("Enter the number of hours to add: "))
  #Ask user for minutes
  minutes = int(input("Enter the number of minutes to add: "))

  #Calculate the time after the user-supplied time has passed.
  time to add = timedelta(hours=hours, minutes=minutes)
new time = (current time + time to add)
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
print("\nCurrent time:",) # 12-hour format with AM/PM
print("Future time after adding", hours, "hours and", minutes, "minutes")

if __name__ == '__main__':
  main()
