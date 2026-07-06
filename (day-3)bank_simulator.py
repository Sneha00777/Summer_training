# data management
pin = "1234"
bank_balance = int(input("enter your bank balance: "))

print("welcome, Please Insert your ATM card")
entered_pin = input("Enter your 4-digit PIN to login: ")
if entered_pin == pin:
    print("\n PIN Verified Successfully! Welcome to your account.")

    option_one = "english selected"
    option_two = "hindi selected"
    langauge = input("enter the language: ")

    if langauge == "english":  
        print(option_one)
    else:
        print(option_two)

    operations = {
        "one": "money_withdrawal",
        "two": "money_deposit"  
    }

    option = input("enter the operation you want to perform: ")

    if option == operations["one"]:
        withdrawn_amt = int(input("enter the amount to be withdrawn: "))
        
        if withdrawn_amt > bank_balance:
            print("insufficient bank balance")
        else:
            bank_balance -= withdrawn_amt  
            print("withdrawal successfull")
            print(f"Current Balance: {bank_balance}")

    elif option == operations["two"]:
        deposit_amt = int(input("enter the amt to be deposited: "))
        bank_balance += deposit_amt 
        print("amt deposit successfull")
        print(f"Current Balance: {bank_balance}")
else:
    print("incorrect PIN try again")