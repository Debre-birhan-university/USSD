balance = 100  # Starting balance

while True:
    print("\nUSSD Menu:")
    print("1. Check Balance")
    print("2. Buy Data")
    print("3. Buy Airtime")
    print("4. Exit")
    
    option = input("Enter option: ")

    # -------------------------------
    # Group 1: Check Balance
    if option == "1":
        input(f"Your current balance is {balance} Birr. ")

    # -------------------------------
    # Group 2: Buy Data
    elif option == "2":
        
        packages = [
            {"mb": 50, "price": 10},
            {"mb": 100, "price": 20},
            {"mb": 150, "price": 30},
            {"mb": 200, "price": 40}
        ]
        print("--Buy Data--")
        for i, pack in enumerate(packages, start=1):
            print(f"{i}. {pack["mb"]}MB for {pack["price"]}Birr")
        print("0. Go back")
        data = input("Which do you want? ")
        try:
            data_num = int(data)
        except Exception as e:
            input(f"Error: {e} ")
        else:
            if data_num == 0:
                pass
            elif data_num - 1 in range(len(packages)):
                if packages[data_num - 1]["price"] <= balance:
                    balance -= packages[data_num - 1]["price"]
                    print(f"You have successfully purchased {packages[data_num - 1]["mb"]}MB for {packages[data_num - 1]["price"]}Birr")
                    input(f"Your current balance is {balance} Birr. ")
                else:
                    input("Insufficient balance! ")
            else:
                input("Invalid input! ")

    # -------------------------------
    # Group 3: Buy Airtime
    elif option == "3":
        print("--Buy Airtime--")
        airtime = input("How much Airtime would you like to purchase? ")
        try:
            airtime_num = int(airtime)
        except Exception as e:
            input(f"Error: {e}")
        else:
            if airtime_num <= balance:
                balance -= airtime_num
                print(f"You have successfully purchased {airtime_num}Birr in Airtime")
                input(f"Your current balance is {balance} Birr. ")
            else:
                input("Insufficient balance!! ")


    # -------------------------------
    # Group 4: Exit & Invalid Input
    elif option == "4":
        exit(0)
    else:
        input("Invalid input!! ")
