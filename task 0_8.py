# This function converts any number into hours and minutes

def time_converter(time):
    hours = time // 60  # converts time to hours
    mins = time % 60    # converts time to minutes

    if (hours == 1) and (mins == 1):
        print(f"{time} will become {hours} hour and {mins} minute.")
    elif (hours == 1) and (mins >=0):
        print(f"{time} will become {hours} hour and {mins} minutes.")
    elif (hours >= 0) and (mins == 1):
        print(f"{time} will become {hours} hours and {mins} minute.")
    else:
        print(f"{time} will become {hours} hours and {mins} minutes.")

number = int(input("Enter a number of your choice: "))
time_converter(number)