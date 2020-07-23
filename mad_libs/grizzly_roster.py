forwards = {"Kyle" : 0, "Mack" : 23, "Michael" : 31 , "Peter" : 32, "Derrick" : 35, "Darius" : 40}

gaurds = {"Timmy" : 1, "Josh" : 3, "Naseem" : 5, "Eddy" : 10, "Freddy" : 24}

name = input("Enter the first name of a Grizzly basketball player:\n")

print(name + " is a guard on the Montana Grizzly basketball team.\nHis jersey number is " + str(gaurds[name])) if name in gaurds else print(name + " is a forward on the Montana Grizzly basketball team.\nHis jersey number is " + str(forwards[name])) if name in forwards else print("There is no one on the Montana Grizzly basketball team with the name: " + name)
