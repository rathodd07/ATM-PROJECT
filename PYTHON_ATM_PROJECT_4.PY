#ATM PROJECT USING PYTHON 
import time
from click import option
print("Please Insert Your CARD:")
time.sleep(5)
password=4567
pin=int(input("Please Enter Your ATM Pin:"))
amount=50000
if pin==password:
    while True:
        print("""
        1==Amount
        2==Withdraw Amount 
        3==Deposit Amount
        4==Exit
        """)
        try:
            option=int(input("please enter your option:"))
        except:
            print("please enter valid option:")

        if option==1:
            print(f"Your current amount is:{amount}")
            print("***~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~***")
        if option==2:
            withdraw_amount=int(input("please enter withdraw amount:")) 
            amount=amount-withdraw_amount
            print(f"{withdraw_amount}.00 amount is debited from your account.")
            print(f"Your updated amount is:{amount}")
            print("***~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~***")
        if option==3:
            deposit_amount=int(input("please enter deposit amount:"))
            amount=amount+deposit_amount
            print(f"{deposit_amount}.00 amount is credited to your account.")
            print(f"Your updated  amount is:{amount}")
            print("***~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~***")
        if option==4:
            break
else:
    print("wrong pin please try again:")


