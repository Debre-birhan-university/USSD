balance = 100  # Starting balance

while True:
    print("\nUSSD Menu:")
    print("1. Check Balance")
    print("2. Buy Data")
    print("3. Buy Airtime")
    print("4. Exit")
    
    option = input("Enter option: ")
    
 
    # Group 1: Check Balance
    if option == "1":
        
      print(f"your current balance is {balance}")

    # Group 2: Buy Data
    elif option == "2":
        
        amount = int(input("enter amount:"))
        print(f"you have successfully redeemed a data package of {amount} birr")

    # Group 3: Buy Airtime
    elif option == "3":
      
        amount = int(input("enter amount:"))
        print(f"you have successfully redeemed an airtime of {amount} birr")
        
    # Group 4: Exit & Invalid Input
    elif option == "4":
        print("thank you for using our service")
    else:
        print("invalid input!")
