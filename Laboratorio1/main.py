"""
06/07/23
J.E.V.A.
class caller and log maker
version: 1.0.2
"""
# we import needed classes/libraries
import trig_class

# we assign important variables
file = "logs.txt"

# We welcome the user
print("welcome to the pi machine! Here we server 3 types of PI!")

while True:  # we start the loop
    print("would you like to order?")
    print("if yes press 'y' if no press 'n'")
    loop_yn = str(input())  # we check if they want to start/restart
    if loop_yn == "y":
        print("What would you like to order?")  # we show the options
        print("Sin Pi, Cos Pi and Tan pi, just say 1, 2 or 3 respectivley.")
        choice = str(input())  # we obtain the wanted opperation
        if choice == "1":  # we run the sin method
            opperation = "sin"
            sin = trig_class.trig().sin_pi()
            print(f"\n here's your pi!: {sin} \n")
            trig_class.logs(file).add_log(f"sin: {sin}")
            pass
        elif choice == "2":  # we run the cos method
            opperation = "cos"
            cos = trig_class.trig().cos_pi()
            print(f"\nHere's your pi!: {cos}\n")
            trig_class.logs(file).add_log(f"cos: {cos}")
            pass
        elif choice == "3":  # we run the tan method
            opperation = "tan"
            tan = trig_class.trig().tan_pi()
            print(f"\nHere's your pi!:{tan}\n")
            trig_class.logs(file).add_log(f"tan: {tan}")
            pass
        else:
            print("Thats not on the menu.")
    elif loop_yn == "n":
        print("Alright, see you again soon!")
        break
    else:
        print("ill give you some more time to think...")

print("here at the Pi machine we like to keep track of the orders")
print("if you check, there should be a folder named 'logs.txt'")
print("all your orders and the time they were ordered should be saved there!")
print("ok thats all, have a great time!")
