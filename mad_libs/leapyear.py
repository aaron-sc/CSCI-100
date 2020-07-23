is_leap_year = False
   
input_year = int(input())

''' Type your code here. '''
if((len(str(input_year)) == 4) and input_year % 4 == 0 and not (str(input_year)[2:] == "00")):
    is_leap_year = True
elif((len(str(input_year)) == 4) and (str(input_year)[2:] == "00" and input_year % 4 == 0 and input_year % 400 == 0)):
    is_leap_year = True
else:
    is_leap_year = False
print(str(input_year) + " - leap year") if (is_leap_year) else print(str(input_year) + " - not a leap year")

print(1900 % 400)