import datetime
import os
import time
import threading
import signal
import sys

counter24or12 = 0
alarmornot = 0
alarm_hour = None 
alarm_minute = None
alarm_second = None

def current_time(): 
    my_datetime = datetime.datetime.today()
    my_time = my_datetime.time()
    if counter24or12 % 2 == 0: 
        c_time = my_time.strftime("%H:%M:%S")
    if counter24or12 % 2 == 1:
        c_time = my_time.strftime("%I:%M:%S%p")
    if alarmornot % 2 == 1:
                alarm(alarm_hour, alarm_minute, alarm_second, my_time.hour, my_time.minute, my_time.second)
    return(c_time)

def display_time(a, b, c):
    d = a
    amorpm = ""
    while True :
        try : 
            if c == 60:
                b +=1
                c = 0
            if b == 60:
                a += 1
                d += 1
                b = 0
            if d == 24:
                d = 0
            if counter24or12 % 2 == 0: 
                if a == 24:
                    a = 0
            if counter24or12 % 2 == 1:
                if a > 12:
                    a -= 12
                if a == 13:
                    a = 1
                if d <= 11:
                    amorpm = "AM"
                if d > 11:
                    amorpm = "PM"
            timer = datetime.time(a, b, c)
            print(timer, amorpm)
            if alarmornot % 2 == 1:
                alarm(alarm_hour, alarm_minute, alarm_second, a, b, c)
            print("ctrl c pour arrêter")
            time.sleep(1)
            os.system('cls')
            c+=1
        except KeyboardInterrupt:
            menu()

def alarm(a_h, a_m, a_s, c_h, c_m, c_s):
    if a_h == c_h:
        if a_m == c_m:
            if a_s == c_s:
                print("it's tiiiiime") 

def setalarm():
    alarm_hour = int(input("heure"))
    alarm_minute = int(input("minute"))
    alarm_second = int(input("second"))
    alarm = (alarm_hour, alarm_minute, alarm_second)
    return(alarm)

t1 = threading.Thread(target=current_time, daemon = True).start()
def menu():
    while 1 == 1:
        print("Bonjour Mamie ! Que veux-tu faire aujourd'hui ?")
        print("1 _ Changer de 12/24h")
        print("2 _ Afficher l'heure actuelle")
        print("3 _ Régler l'heure")
        print("4 _ Régler l'alarme")
        print("5 _ Arrêter le temps")
        print("6 _ Sortir")
        answermenu = int(input())
        if answermenu == 1:
            global counter24or12
            counter24or12 += 1
        if answermenu == 2:
            os.system('cls')
            while 1 == 1 :
                try : 
                    my_time = current_time()
                    print(my_time)
                    global alarmornot
                    global alarm_hour
                    global alarm_minute
                    global alarm_second
                    print("ctrl c pour arrêter")
                    time.sleep(1)
                    os.system('cls')
                except KeyboardInterrupt:
                    menu()
        if answermenu == 3:
            os.system('cls')
            display_time_hour = int(input("heure"))
            display_time_minute = int(input("heure"))
            display_time_second = int(input("heure"))
            display_time(display_time_hour, display_time_minute, display_time_second)
        if answermenu == 4:
            os.system('cls')
            alarmornot += 1
            alarm = setalarm()
            alarm_hour = alarm[0]
            alarm_minute = alarm[1]
            alarm_second = alarm[2]
            print("alarme activée")
        
        if answermenu == 6:
            print("Bonne journée Mamie !")
            exit()
            
menu()

