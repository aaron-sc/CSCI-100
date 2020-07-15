seconds = int(input("Enter the number of seconds: "))

hours = seconds//3600

seconds = seconds%3600

mins = seconds//60

seconds = seconds%60


print("Hours: " + str(hours) + "\nMinutes: " + str(mins) + "\nSeconds: " + str(seconds))