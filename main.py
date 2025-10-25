balance = 100  # Starting balance
while True:
    print("\nUSSD Menu:")
    print("1. Check Balance")
    print("2. Buy Data")
    print("3. Buy Airtime")
    print("4. Deposite Balance ")
    print("5. Exit")
    option = input("Enter option: ")

    if option == "1":
        print (f"Your available balance is:" ,balance,"ETB")
        break
    elif option == "2":
        phone=input("Enter recharged mobile number: ") #use 0912345678 to be identical with our phone
        if phone =="0912345678":
            amount=int(input("Enter your amount: "))
            if amount<=balance:
                balance=balance-amount
                print("Successful,You buy", amount,"ETB Data pakege and Your current balance is ",balance,"ETB")
            else:
                print ("Your balance is insufficient.")
        else:
            print ("Incorrect phone number,Please try again!")
        break
    elif option == "3":
        phone=input("Enter recharged mobile number: ") #use 0912345678 to be identical with our phone
        if phone =="0912345678":
            amount=int(input("Enter your amount: "))
            if amount<=balance:
                balance=balance-amount
                print("Successful,You buy", amount,"ETB air time and Your current balance is ",balance,"ETB")
            else:
                print ("Your balance is insufficient.")
        else:
            print ("Incorrect phone number,Please try again!")
        break
    elif option == "4":
       deposite=int(input("Enter Deposit amount: "))
       balance=balance+deposite
       print("Successful,You deposite", deposite,"ETB and Your current balance is ",balance,"ETB")
       break
    elif option == "5":
        print ("Good bay.")
        break
    else:
       print("Please insert correct option.")
