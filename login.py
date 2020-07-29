print("Welcome to my secret program!")


logins = {"python" : "csci135"}

for x in range(3):
    print()

    u_name = input("Please enter your username: ")
    u_pass = input("Please enter your password: ")

    if(u_name in logins):
        if(logins[u_name] != u_pass):
            print("Invalid password")
        else:
            print("\nThanks for entering the correct username and password!\nI hope you have a GREAT day!!")
            break
    elif (u_pass in list(logins.values())):
        print("Invalid username")
    else:
        print("Invalid username and password")
    if(x==2):
        print("\nToo many attempts!  You are locked out!")
        break