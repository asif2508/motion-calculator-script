import sys
import times
import acceleration
import displacement
import velocity
import utter
def about():
    print("--------------------------------------------------------------")
    print('''This is a motion calculator developed by Rakibul Hasan Asif.''')
    print('''            contact: rakibul4210@gmail.com''')
    print("--------------------------------------------------------------")
def help():
    print("This is the details of input: ")
    print("--------------------------------")
    print("1. s stands for displacement.")
    print("2. u stands fo initial velocity.")
    print("3. v stands for velocity.")
    print("4. t stands for time.")
    print("5. a stands for acceleration.")
    print("----------------------------------")
    print("Enter values to get result in every step.")
    print("      All the best and Thank You!")
    print("-----------------------------------")
def main_calc():
    print("***Thanks for choosing me***")
    print("Now choose what you like to calculate:")
    print("-----------------------------------------")
    print("1. Displacement")
    print("2. Velocity")
    print("3. Time")
    print("4. Initial velocity")
    print("5. Acceleration")
    like = int(input("Enter your choice(ex: 1,2,3,4 or 5): "))
    
    if like == 1:
        displacement.distance_main()
    elif like == 2:
        velocity.velocity_main()
    elif like == 3:
        times.time_main()
    elif like == 4:
        utter.intial_vel_main()
    elif like == 5:
        acceleration.acceleration_main()
    else:
        print("Invalid choice :(")
    
    
    
    
def menu():
    try:
        print("******************************")
        print("WELCOME TO THE WORLD OF MOTION")
        print("  DEV BY RAKIBUL HASAN ASIF")
        print("******************************")
        print("Which one do you prefer to look at:")
        print("1. Main Calculator")
        print("2. Help menu")
        print("3. About")
        print("4. Exit")
        print("-----------------")
        opt = int(input("Enter your choice: "))
        if opt == 1:
            main_calc()
        elif opt == 2:
            help()
        elif opt == 3:
            about()
        elif opt == 4:
            print("Thanks for using me :)")
            sys.exit()
        else:
            print("Invalid choice!")
    except KeyboardInterrupt:
        print("")
        print("Keyboard Interrupted!")
        sys.exit()
try:
    menu()
    try:
        while True:
            run = input("Do you want to run again?(y or n): ")
            if run.lower() == 'y':
                menu()
            elif run.lower() == 'n':
                print("")
                print("Thanks a lot for using me. Have a good day:)")
                sys.exit()
            else:
                print("")
                print("Invalid Input! Please Enter y(yes) or n(no)!")
                sys.exit()
    except KeyboardInterrupt:
        print("")
        print("Keyboard Interrupted!")
        sys.exit()
except ValueError:
    print("Please Enter a correct option!")





