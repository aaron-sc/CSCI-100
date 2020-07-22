direction = {1 : "north/south", 0 : "east/west"}

highway_number = int(input())
toPrint = "I-" + str(highway_number) + " is "

valid = True

if(highway_number > 999 or highway_number <= 0):
    valid = False

if(highway_number <= 99):
    toPrint += "primary, going "

else:
    primary = str(int(str(highway_number)[1:]))
    toPrint += "auxiliary, serving I-"+primary+", going "

toPrint += direction[(highway_number % 2)] + "."


if(valid):
    print(toPrint)
else:
    print(str(highway_number) + " is not a valid interstate highway number.")