menu = ""
while menu != "basta":
    menu=input("cosa vuoi mangiare? ").lower()
    if menu == "pasta":
        print("con il pomodoro?")
    elif menu == "lasagna":
        print("bianca?")
    elif menu == "orecchiette":
        print("con le cime di rapa?")
    elif menu == "basta":
        print("torno piu' tardi")
    else:
        print("non ho capito")
i=0
while i < 5:
    print("i e':", i)
    i += 1
