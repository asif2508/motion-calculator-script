import math
global a, s, u, v, t
# distance_1 s= ut+ .5*a*t^2
def distance_1():
    a = float(input("Enter the value of a: "))
    u = float(input("Enter the value of u: "))
    t = float(input("Enter the value of t: "))
    s = (u * t) + (0.5 * a * (t * t))
    s = abs(s)
    print(f"The value of distance is {s} m.")


# distance_2 s = (pow(v,2)-pow(u,2))/(2*a)
def distance_2():
    a = float(input("Enter the value of a: "))
    u = float(input("Enter the value of u: "))
    v = float(input("Enter the value of v: "))
    s = (pow(v, 2) - pow(u, 2)) / (2 * a)
    s = abs(s)
    print(f"The value of distance is {s} m.")


# distance_3 s = vt
def distance_3():
    v = float(input("Enter the value of v: "))
    t = float(input("Enter the value of t: "))
    s = v * t
    s = abs(s)
    print(f"The value of distance is {s} m.")


# distance_4 s = .5*(u+v)*t
def distance_4():
    u = float(input("Enter the value of u: "))
    v = float(input("Enter the value of v: "))
    t = float(input("Enter the value of t: "))
    s = 0.5 * (u + v) * t
    s = abs(s)
    print(f"The value of distance is {s} m.")
def distance_main():
    print("Which values do you have?")
    print("1. a, u and t")
    print("2. a, u and v")
    print("3. v and u")
    print("4. u, v and t")
    print("------------------")
    choice = int(input("Enter Your choice(ex: 1,2,3 or 4): "))
    if choice == 1:
        distance_1()
    elif choice == 2:
        distance_2()
    elif choice == 3:
        distance_3()
    elif choice == 4:
        distance_4()
    else:
        print("Invalid choice!")
