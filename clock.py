import datetime
import os
import time

def current_time():
    i = 0
    while i == 0:
        my_datetime = datetime.datetime.today()

        my_time = my_datetime.time()
        if twelveortwentyfour == "24" : 
            c_time = my_time.strftime("%H:%M:%S")
        if twelveortwentyfour == "12" :
            c_time = my_time.strftime("%I:%M:%S%p")
        os.system('cls')
        print(c_time)
        if answer1 == "oui":
            alarm(alarm_hour, alarm_minute, alarm_second, my_time.hour, my_time.minute, my_time.second)
        time.sleep(1)

def display_time(a, b, c):
    d = a
    while 1 == 1:
        amorpm = ""
        if c == 60:
            b +=1
            c = 0
        if b == 60:
            a += 1
            d += 1
            b = 0
        if d == 24:
            d = 0
        if twelveortwentyfour == "24":
            if a == 24:
                a = 0
        if twelveortwentyfour == "12":
            if a > 12:
                a -= 12
            if a == 13:
                a = 1
            if d <= 11:
                amorpm = "AM"
            if d > 11:
                amorpm = "PM"
        timer = datetime.time(a, b, c)
        os.system('cls')
        print(timer, amorpm)

        if answer1 == "oui":
            if twelveortwentyfour == "12":
                if amorpm == "PM":
                    a +=12
            alarm(alarm_hour, alarm_minute, alarm_second, a, b, c)
        c +=1
        time.sleep(1)

def alarm(a_h, a_m, a_s, c_h, c_m, c_s):
    if a_h == c_h:
        if a_m == c_m:
            if a_s == c_s:
                print("it's tiiiiime") 

print("Bonjour Mamie ! Que veux tu faire aujourd'hui ?")
twelveortwentyfour = input("Veux-tu mettre le temps en 24h ou en 12h ?(24/12)")
answer = input("Veux-tu afficher l'heure actuelle ? (oui/non)")
if answer == "oui":
    answer1 = input("Veux tu régler une alarme ? (oui/non)")
    if answer1 == "oui":
        alarm_hour = int(input("heure:"))
        alarm_minute = int(input("minute : "))
        alarm_second = int(input("second :"))
    current_time()
if answer == "non":
    answer2 = input("Veux-tu régler l'heure ?(oui/non)")
    if answer2 == "oui":
        display_time_hour = int(input("heure :"))
        display_time_minute = int(input("minute :"))
        display_time_second = int(input("seconde :"))
        answer1 = input("Veux tu régler une alarme ? (oui/non)")
        if answer1 == "oui":
            print("entrez l'heure de l'alarme sous format HH:MM:SS")
            alarm_hour = int(input("heure:"))
            alarm_minute = int(input("minute : "))
            alarm_second = int(input("second :"))
        display_time(display_time_hour, display_time_minute, display_time_second)
    if answer2 == "non" :
        print("bonne journée mamie !")
