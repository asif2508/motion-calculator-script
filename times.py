import math
global a, s, u, v, t
#time_1 t = (v-u)/a
def time_1():
    u = float(input("Enter the value of u: "))
    v = float(input("Enter the value of v: "))
    a = float(input("Enter the value of a: "))
    t = (v-u)/a
    t = abs(t)
    print(f"The value of time is {t} s")

# time_2 t = s/v
def time_2():
    s = float(input("Enter the value of s: "))
    v = float(input("Enter the value of v: "))
    t = s/v
    t = abs(t)
    print(f"The value of time is {t} s")
# time_3 t = (2*s)/(u+v)
def time_3():
    u = float(input("Enter the value of u: "))
    v = float(input("Enter the value of v: "))
    s = float(input("Enter the value of s: "))
    t = (2*s)/(u+v)
    t = abs(t)
    print(f"The value of time is {t} s")
#time_4 t = math.sqrt((2*s)/a) if u = 0
def time_4():
    s = float(input("Enter the value of s: "))
    a = float(input("Enter the value of a: "))
    try:
        t = math.sqrt((2*s)/a)
        t = abs(t)
        print(f"The value of time is {t} s")
    except ValueError:
        print("We can't use negative acceleration with this equation.")
def time_main():
    print("which values do you have?")
    print("1. u, v and a")
    print("2. s and v")
    print("3. u, v and s")
    print("4. s and a where u = 0")
    print("------------------------")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        time_1()
    elif choice == 2:
        time_2()
    elif choice == 3:
        time_3()
    elif choice == 4:
        time_4()
    else:
        print("Invalid choice!")