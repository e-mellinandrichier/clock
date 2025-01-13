import datetime
import time


def alarm(a_h,a_m,a_s,c_h,c_m,c_s):
    if a_h == c_h :
        if a_m == c_m :
                if a_s == c_s :
                    print("Wake up")


def display_time():
    hour_period = a   
    hours = int(input("Please choose the hour you wish to set up your time ? "))
    minutes = int(input("Please choose the minutes (0-59):"))
    seconds = int(input("Please choose the seconds (o-60):"))
    while 1 == 1 :
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0
        timer = datetime.time(hours,minutes,seconds)
        if hour_period == 12 and hours > 12 :
            print(current_time)
        if hour_period == 24 and hours == 24:
            print(current_time2)
        if hour_period == 12:
            period = "AM" if hours < 12 else "PM"
        if hour_period == 12 and hours > 12 : 
            hours %= 12
        print(timer)
        if answer == "yes":
            alarm (alarm_hours,alarm_minutes,alarm_seconds,hours,minutes,seconds)
        seconds += 1
        time.sleep(1)  

def current_hour():
    a = 1
    while a :
        c = datetime.datetime.now()
        current_time = c.strftime('%H:%M:%S')
        current_time2 = c.strftime('')
        print("Current time is :", current_time)
        if answer == "yes":
            alarm (alarm_hours,alarm_minutes,alarm_seconds,c.hour,c.minute,c.second)
        time.sleep(1)
    

print("Hello and welcome into your clock first do you wish an alarm ?")
answer = input("Answer by yes or no")
if answer == "yes":
    alarm_hours = int(input("Please choose the hour"))
    alarm_minutes = int(input("Please choose the minutes"))
    alarm_seconds = int(input("Please choose the seconds"))
if answer == "no":
    print()
answer2 = input("Ok great, now do you wish to set up the time ? If you say no, you will have the current time ! ")
if answer2 == "yes":
    display_time()
if answer2 == "no":
    current_hour()



