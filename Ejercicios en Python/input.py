problem= str(input("¿you have a problem? yes / no: "))
end="Problem Solved"
if problem == "yes":
    print("Use a gun")
    work=str(input("¿Did it work? yes / no: "))
    while(work == "no"):
        print("Use more guns")
        work=str(input("¿Did it work? yes / no: "))
        if work == "yes":
            print(end)
elif problem == "no":
    print(end)