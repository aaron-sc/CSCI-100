#name: Aaron Santa Cruz
#class: csci100
#date: 8/12/2020
#project: matplotlib activity 
#sources: https://www.co2.earth/co2-datasets

#import statement
import matplotlib.pyplot as plt
import os 

# For some reason, I need to get the cwd
dir_path = os.path.dirname(os.path.realpath(__file__))

f = open(dir_path + "/co2.txt", "r")
contents = f.read()

co2 = {}

# Turn the data into co2["year"] = "ppm"
for i, data in enumerate(contents.split("\n")):
    if(i != 0 and i % 3 == 0):
        nums = data.split()
        co2[nums[0]] = nums[1]

#prepare the data 
x = list(co2.keys())
y = list(co2.values())

#plot function 
plt.plot(x, y, label="ppm")

#add title
plt.title("CO2 Emmisions per year")

#add legend 
plt.legend()

# Change the size of the labels
plt.tick_params(axis='x', which='major', labelsize=5)
plt.tick_params(axis='y', which='major', labelsize=5)
plt.tight_layout()

# Add axis labels
plt.xlabel("Year")
plt.ylabel("ppm")

#function to show the plot
plt.show() 