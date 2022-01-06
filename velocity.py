import math
global a, s, u, v, t
# velocity_1 v = u + at
def velocity_1():
    u = float(input("Enter the value of u: "))
    t = float(input("Enter the value of t: "))
    a = float(input("Enter the value of a: "))
    v = u + (a * t)
    v = abs(v)
    print(f"The value of velocity {v} m/s")


# velocity_2 v = sqrt(pow(u,2) + (2*a*s))
def velocity_2():
    u = float(input("Enter the value of u: "))
    s = float(input("Enter the value of s: "))
    a = float(input("Enter the value of a: "))
    v = math.sqrt(pow(u, 2) + (2 * a * s))
    v = abs(v)
    print(f"The value of velocity {v} m/s")


# velocity_3 v = s/t
def velocity_3():
    s = float(input("Enter the value of s: "))
    t = float(input("Enter the value of t: "))
    v = s / t
    print(f"The value of velocity {v} m/s")


# velocity_4 v = ((2*s)/t)-u
def velocity_4():
    s = float(input("Enter the value of s: "))
    t = float(input("Enter the value of t: "))
    u = float(input("Enter the value of u: "))
    v = ((2 * s) / t) - u
    print(f"The value of velocity {v} m/s")
#velocity_main function

def velocity_main():
    print("Which values do you have?")
    print("1. u, t and a")
    print("2. u, s and a")
    print("3. s and t")
    print("4. s, t and u")
    print("-----------------")
    choice = int(input("Enter your choice(ex: 1,2,3 or 4): "))
    if choice == 1:
        velocity_1()
    elif choice == 2:
        velocity_2()
    elif choice == 3:
        velocity_3()
    elif choice == 4:
        velocity_4()
    else:
        print("Invalid choice!")

