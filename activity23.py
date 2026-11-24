shonen = []
korean = []
isekai = []
adventure = []
fantasy = []

while True:
    ans = input("Do you watch anime -->? yes or no ").lower()

    if ans == "yes":
        print("what kind of anime do you watch")
        print("1-shonen \n2 korean \n3 isekai \n4 adventure \n5 fantasy")

        choice = int(input("Input ----> "))

        if choice == 1:
            print("shonen")
            title = input("Please input the title of the ANime ----> " )
            shonen.append(title)
            print("List of shonen")
            print(shonen)
        elif choice == 1:
            title = input("What do you want to change")
            if title in shonen:
                shonen.remove(title)
                print(title, "removed")
            else:
                print(title, "not in the list")
            
            
            con = input("Do you wish to continue yes / no").lower()

            if con == "yes":
                continue
            else:
                break
        else:
            print("INVALID CHOICE")
