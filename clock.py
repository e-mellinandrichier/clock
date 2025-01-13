#datetime library
import datetime
#used to clear the terminal
import os
#used to make the loop sleep during 1 second
import time

#global variables that will be used throughout the script
counter24or12 = 0
alarmornot = 0
timestop = 0
alarm_hour = None 
alarm_minute = None
alarm_second = None

#function to display the current time
def current_time(): 
    #getting the date and time of today in the my_datetime variable
    my_datetime = datetime.datetime.today()
    #getting only the time thanks to the .time()method on our variable my_datetime and putting it in my_time
    my_time = my_datetime.time()
    if counter24or12 % 2 == 0: 
        #if counter24or12 is even, the time will be displayed in the 24h system
        #it is stocked in the c_time variable 
        c_time = my_time.strftime("%H:%M:%S")
    if counter24or12 % 2 == 1:
        #if counter24or12 is odd, it will be in the 12h system
        c_time = my_time.strftime("%I:%M:%S%p")
        #if an alarm is set, we call the alarm method with the chosen alarm time, along with the current hour (my_time.hour), minute and second
    if alarmornot % 2 == 1:
                alarm(alarm_hour, alarm_minute, alarm_second, my_time.hour, my_time.minute, my_time.second)
    # returns the c_time variable, containing either the 24 or the 12 hour
    return(c_time)

def display_time(a, b, c):
    #the d variable will be used to display the 12h system time
    d = a
    # the amorpm variable will be used to display either AM or PM
    amorpm = ""
    # we do an infinite loop to print something 
    while True :
        try : 
            #on each 60 second that pass, we increment the b (minute)variable by one. 
            if c == 60:
                b +=1
                c = 0
                # on each 60 minutes that pass, we increment the c (hour) variable by one
            if b == 60:
                a += 1
                d += 1
                b = 0
            # if the d variable is equal to 24 (midnight), it will go back to 0
            if d == 24:
                d = 0
            # if the user choses the 24h time system, at midnight the hour will be set to 0
            if counter24or12 % 2 == 0:
                if a == 24:
                    a = 0
            # if the user choses the 12h time system, 
            if counter24or12 % 2 == 1:
                # on each 12h, the hour will be back to 1
                if a > 12:
                    a -= 12
                if a == 13:
                    a = 1
                # the d variable is used here to know if it's the morning or the evening
                if d <= 11:
                    amorpm = "AM"
                if d > 11:
                    amorpm = "PM"
            # in the timer variable, a b and c are sotcked and displayed the right way (with the .time() method)
            timer = datetime.time(a, b, c)
            # printing the timer variable, along with the amorpm variable containing either "AM" or "PM"
            print(timer, amorpm)
            # if the time stop option is selected, the loop stops
            if timestop % 2 == 1:
                break
            # if the alarm option is selected, we call the alarm function with the right arguments
            if alarmornot % 2 == 1:
                alarm(alarm_hour, alarm_minute, alarm_second, a, b, c)
            print("ctrl c pour arrêter")
            #we do the loop one time per sec
            time.sleep(1)
            # we clear the terminal
            os.system('cls')
            # c (seconds)incrementing by one (each second)
            c+=1
        # if the user does ctrl c, we will go back to the menu
        except KeyboardInterrupt:
            menu()

def alarm(a_h, a_m, a_s, c_h, c_m, c_s):
    # if the alarm hour is the same as the current hour
    if a_h == c_h:
        # if the alarm minute is the same as the current minute
        if a_m == c_m:
            # if the alarm second is the same as the current second
            if a_s == c_s:
                # we print the alarm message
                print("it's tiiiiime") 

def setalarm():
    # if the user sets an alarm, they can chose the time of the alarm
    alarm_hour = int(input("heure"))
    alarm_minute = int(input("minute"))
    alarm_second = int(input("second"))
    # we stock it in the alarm variable as a tuple
    alarm = (alarm_hour, alarm_minute, alarm_second)
    # returns that tuple
    return(alarm)

def menu():
    # infinite loop
    while 1 == 1:
        print("Bonjour Mamie ! Que veux-tu faire aujourd'hui ?")
        print("1 _ Changer de 12/24h")
        print("2 _ Afficher l'heure actuelle")
        print("3 _ Régler l'heure")
        print("4 _ Régler l'alarme")
        print("5 _ Arrêter le temps")
        print("6 _ Sortir")
        # the input of the user is put in the answermenu variable
        answermenu = int(input())
        if answermenu == 1:
            global counter24or12
            counter24or12 += 1
        if answermenu == 2:
            os.system('cls')
            #inifinite loop
            while 1 == 1 :
                try :
                    # in the my_time variable, we stock the tuple that the current_time() method returns
                    my_time = current_time()
                    print(my_time)
                    # the global variables that will be needed in the current_time() function
                    global timestop
                    global alarmornot
                    global alarm_hour
                    global alarm_minute
                    global alarm_second
                    print("ctrl c pour arrêter")
                    # the loop stops for 1 sec
                    time.sleep(1)
                    os.system('cls')
                    # if the time stop option is selected, the loop breaks
                    if timestop % 2 == 1:
                        break
                except KeyboardInterrupt:
                    menu()
        if answermenu == 3:
            # in the global variables, we stock the input result
            display_time_hour = int(input("Heure"))
            display_time_minute = int(input("Minute"))
            display_time_second = int(input("Seconde"))
            os.system('cls')
            # and we call the display_time function with the inputs as the arg
            display_time(display_time_hour, display_time_minute, display_time_second)
            
        if answermenu == 4:
            os.system('cls')
            # the alarm option is selected, that will be used later in the current_time() or the display_time() function
            alarmornot += 1
            # we take the values returned by the setalarm() and we put it in the alarm variable
            alarm = setalarm()
            # in the alarm_hour variable, we stock the first value contained in the alarm variable, which corresponds to the hour
            alarm_hour = alarm[0]
            # in the alarm_minute variable, we stock the first value contained in the alarm variable, which corresponds to the minute
            alarm_minute = alarm[1]
            # in the alarm_second variable, we stock the first value contained in the alarm variable, which corresponds to the second
            alarm_second = alarm[2]
            print("Alarme activée")

        if answermenu == 5:
            timestop +=1 
        
        if answermenu == 6:
            print("Bonne journée Mamie !")
            exit()
# we execute the menu() function
menu()