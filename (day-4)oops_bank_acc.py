#student information system
class bank_account:
    #name = "sneha"
    #account_no = "1234567890"
    #balance = 23549
    def acc_info(i,name="",account_no="",balance=" "):
        i.name=name
        i.account_no=account_no
        i.balance=int(balance)
    def deposit(i):
        a=int(input("enter the amount to be deposited:"))
        i.balance=i.balance+a
        print(f"updated balance:{i.balance}")
    def withdraw(i):
        b=int(input("enter the amount to be withdrawn:"))
        if b>i.balance:
            print("withdrawal is more than balance")
        else:
            i.balance=i.balance-b
            print(f"updated balance:{i.balance}")
    def display_balance(i):
        print(f"Your balance is:{i.balance}")
x=bank_account()
x.acc_info("sneha","1234567890",23549)
x.deposit()
x.withdraw()
x.display_balance()