usr_time = float(input("What hour of the day is it? (0-23) "))

if usr_time <= 5:
    print("It's early. You should be sleeping!")
elif usr_time <= 7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast...")
elif usr_time <= 9:
    print("Time to go to work.")
elif usr_time <= 12:
    print("You should be working!")
elif usr_time <= 13:
    print("Take your lunch break!")
elif usr_time <= 17:
    print("Do you feel that afternoon lull?")
elif usr_time <= 19:
    print("Time to hit the gym...")
elif usr_time <= 21:
    print("Gotta eat that dinner.")
elif usr_time <= 23:
    print("Get that SLEEP. And rePEAT!")
else:
    print("You didn't type an acceptable value! (0-23)")