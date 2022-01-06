import math
global a, s, u, v, t
# acceleration_1 a = (v-u)/t
def acceleration_1():
    u = float(input("Enter the value of u: "))
    v = float(input("Enter the value of v: "))
    t = float(input("Enter the value of t: "))
    a = (v-u)/t
    print(f"The value of acceleration is {a} m/s^2")

#acceleration_2 a = (pow(v,2)- pow(u,2))/(2*s)
def acceleration_2():
    u = float(input("Enter the value of u: "))
    v = float(input("Enter the value of v: "))
    s = float(input("Enter the value of s: "))
    a = (pow(v,2)- pow(u,2))/(2*s)
    print(f"The value of acceleration is {a} m/s^2")
# acceleration_3 a = (2*(s-(u*t)))/ pow(t,2)
def acceleration_3():
    s = float(input("Enter the value of s: "))
    t = float(input("Enter the value of t: "))
    u = float(input("Enter the value of u: "))
    a = (2*(s-(u*t)))/ pow(t,2)
    print(f"The value of acceleration is {a} m/s^2")

#acceleration main function
def acceleration_main():
    print("Which values do you have?")
    print("1. u, v and t")
    print("2. u, v and s")
    print("3. s, t and u")
    print("----------------")
    choice = int(input("Enter Your choice(ex: 1,2 or 3): "))
    if choice == 1:
        acceleration_1()
    elif choice == 2:
        acceleration_2()
    elif choice == 3:
        acceleration_3
    else:
        print("Invalid choice!")
