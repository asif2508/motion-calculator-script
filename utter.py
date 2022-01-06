import math
global s,u,v,t,a
#intial_vel_1 u = (s - (.5*a* pow(t,2)))/t
def intial_vel_1():
    s = float(input("Enter the value of s: "))
    t = float(input("Enter the value of t: "))
    a = float(input("Enter the value of a: "))
    u = (s - (.5*a* pow(t,2)))/t
    u = abs(u)
    print(f"The value of velocity {u} m/s")
#intial_vel_2 u = math.sqrt(pow(v,2) - (2*a*s))
def intial_vel_2():
    s = float(input("Enter the value of s: "))
    v = float(input("Enter the value of v: "))
    a = float(input("Enter the value of a: "))
    try:
        u = pow(v,2)-(2*a*s)
        u = math.sqrt(u)
        u = abs(u)
        print(f"The value of velocity {u} m/s")
        pass
    except ValueError:
        print("Here v^2 is less than (2*a*s). So not possible in this way.")
        pass
#intial_vel_3 u = v - (a*t)
def intial_vel_3():
    t = float(input("Enter the value of t: "))
    v = float(input("Enter the value of v: "))
    a = float(input("Enter the value of a: "))
    u = v - (a*t)
    u = abs(u)
    print(f"The value of velocity {u} m/s")
#intial_vel_4 u = ((2*s)/t) - v
def intial_vel_4():
    t = float(input("Enter the value of t: "))
    v = float(input("Enter the value of v: "))
    s = float(input("Enter the value of s: "))
    u = ((2*s)/t) - v
    u = abs(u)
    print(f"The value of velocity {u} m/s")
#intial_main
def intial_vel_main():
    print("Which values do you have?")
    print("1. s, t and a")
    print("2. s, v and a")
    print("3. t, v and a")
    print("4. t, v and s")
    print("-----------------")
    choice = int(input("Enter Your choice(ex: 1,2,3 or 4): "))
    if choice == 1:
        intial_vel_1()
    elif choice == 2:
        intial_vel_2()
    elif choice == 3:
        intial_vel_3()
    elif choice == 4:
        intial_vel_4()
    else:
        print("Invalid choice!")









