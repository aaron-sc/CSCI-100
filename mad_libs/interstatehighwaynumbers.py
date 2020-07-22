direction = {1 : "north/south", 0 : "east/west"}

num = int(input())
toPrint = "I-" + str(num) + " is "

if(num <= 99):
    toPrint += "primary, going "
else:
    primary = str(int(str(num)[1:]))
    toPrint += "auxiliary, serving I-"+primary+", going "

toPrint += direction[(num % 2)] + "."

print(toPrint)