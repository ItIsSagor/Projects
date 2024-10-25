from datetime import datetime
from abc import ABC

class User(ABC):
    def __init__(self, name, email, address, acc_type):
        self.name = name
        self.email = email
        self.address = address
        self.acc_type = acc_type

class AccHolder(User):
    def __init__(self, bank, name, email, address, acc_type):
        super().__init__(name, email, address, acc_type)
        self.__balance = 0
        self.__history = []
        self.acc_id = len(bank.accholders) + 1
        self.loan_times = 0

    def add_acc_holder(self, bank):
        bank.add_acc_holder(self)

    def available_balance(self):
        print('\n------------------------------')
        print(f'Your Balance is: {self.__balance}')
        print('------------------------------\n')
    
    def deposit(self, bank, amount):
        if bank.bankrupt_feature:
            self.__balance += amount
            bank.total_balance += amount
            self.__history.append((datetime.now(), '<-- Deposit -->', amount))
            print('\n--------------------------------------------')
            print(f'Amount {amount} is deposit successfull !!')
            print(f'New Balance: {self.__balance}')
            print('--------------------------------------------\n')
        else:
            print('\n------------------------------')
            print('The bank is bankrupt!!!')
            print('------------------------------\n')

    def withdraw(self, bank, amount):
        if bank.bankrupt_feature:
            if amount <= self.__balance:
                self.__balance -= amount
                bank.total_balance -= amount
                self.__history.append((datetime.now(), '<-- Withdraw -->', amount))
                print('\n--------------------------------------')
                print(f'Amount: {amount} withdraw successful.')
                print(f'New Balance: {self.__balance}')
                print('--------------------------------------\n')
            else:
                print('\n------------------------------')
                print('Withdrawal amount exceeded.')
                print('------------------------------\n')
        else:
            print('\n------------------------------')
            print('The bank is bankrupt!!!')
            print('------------------------------\n')

    def transfer_money(self, bank, amount, id):
        if bank.bankrupt_feature:
            getid = bank.find_id(id)
            if getid:
                if amount <= self.__balance:
                    self.__balance -= amount
                    self.__history.append((datetime.now(), '<-- Transfer -->', amount))
                    print('\n-----------------------------------------')
                    print(f'Amount {amount} successfully transfered.\nNew balance: {self.__balance}')
                    print('-----------------------------------------\n')
                else:
                    print('\n------------------------------')
                    print('Transfer amount exceeded!!!')
                    print('------------------------------\n')
            else:
                print('\n------------------------------')
                print('Account does not exist!!!')
                print('------------------------------\n')
        else:
            print('\n------------------------------')
            print('The bank is bankrupt!!!')
            print('------------------------------\n')

    def take_loan(self, bank, amount):
        if bank.bankrupt_feature:
            if bank.loan_feature:
                if self.loan_times < 2:
                    self.__balance += amount
                    bank.total_balance -= amount
                    bank.total_loan += amount
                    self.loan_times += 1
                    self.__history.append((datetime.now(), '<-- Loan -->', amount))
                    print('\n-------------------------------------------')
                    print(f'Amount {amount} successfully taken as loan.\nNew balance: {self.__balance}')
                    print('-------------------------------------------\n')
                else:
                    print('\n------------------------------')
                    print('Loan limit exceeded!!!')
                    print('------------------------------\n')
            else:
                print('\n-----------------------------------------')
                print('Loan feature is currently turned off!!!')
                print('-----------------------------------------\n')
        else:
            print('\n------------------------------')
            print('The bank is bankrupt!!!')
            print('------------------------------\n')
    
    def transaction_history(self):
        if self.__history:
            print('\n\t\tTrasaction History')
            print('-----------------------------------------------------')
            for hstry in self.__history:
                print(f'{hstry[0]} {hstry[1]} {hstry[2]}')
            print('-----------------------------------------------------\n')
        else:
            print('\n------------------------------')
            print('No Transaction Yet!!!')
            print('------------------------------\n')



class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address, acc_type = None)

    def show_all_user(self, bank):
        bank.show_all_user()

    def delete_an_account(self, bank, accid):
        bank.delete_an_account(accid)
    
    def check_total_balance(self, bank):
        print('\n----------------------------------------')
        print(f'Available Balance: {bank.total_balance}')
        print('----------------------------------------\n')
        
    def check_loan_amount(self, bank):
        print('\n------------------------------------')
        print(f'Total Loan amount: {bank.total_loan}')
        print('------------------------------------\n')

    def on_off(self, bank, status):
        if status == 'ON':
            bank.loan_feature = True
        else:
            bank.loan_feature = False

        if bank.loan_feature == True:
            print('\n------------------------------')
            print('Loan feature has been ON')
            print('------------------------------\n')
        else:
            print('\n------------------------------')
            print('Loan feature has been OFF.')
            print('------------------------------\n')


    def bankrupt_on_off(self, bank, status):
        if status == 'ON':
            bank.bankrupt_feature = True
        else:
            bank.bankrupt_feature = False

        if bank.bankrupt_feature == True:
            print('\n------------------------------')
            print('Bankrupt feature has been ON')
            print('------------------------------\n')
        else:
            print('\n------------------------------')
            print('Bankrupt feature has been OFF.')
            print('------------------------------')

    def loan_status(self, bank):
        if bank.loan_feature == True:
            print('\n------------------------------')
            print('For loan, Current status is ON.')
            print('------------------------------\n')
        else:
            print('\n------------------------------')
            print('For Loan, Current Status is OFF.')
            print('------------------------------\n')

    def bankrupt(self, bank):
        if bank.bankrupt_feature == True:
            print('\n------------------------------')
            print('For Bankrupt, Current status is ON.')
            print('------------------------------')
        else:
            print('\n------------------------------')
            print('For Bankrupt, Current Status is OFF.')
            print('------------------------------\n')


class Bank:
    def __init__(self, name):
        self.name = name
        self.accholders = []
        self.total_balance = 10000
        self.total_loan = 0
        self.loan_feature = True
        self.bankrupt_feature = True
        
    def add_acc_holder(self, accholder):
        self.accholders.append(accholder)
        print('\n------------------------------')
        print(f'Account added successfull')
        print('------------------------------\n')
    
    def show_all_user(self):
        print('\n\t\tOur User List!!')
        if self.accholders:
            print('------------------------------------------------------------------------')
            for cus in self.accholders:
                print(f'Account_ID: {cus.acc_id} <--> Name : {cus.name} <--> Email : {cus.email}')
            print('------------------------------------------------------------------------\n')
        else:
            print('\n-------------------------------------------')
            print('Did not found any user/account holder!!!')
            print('-------------------------------------------\n')

    def find_id(self, accid):
        for id in self.accholders:
            if id.acc_id == accid:
                return id
        return None

    def delete_an_account(self, accid):
        for id in self.accholders:
            if id.acc_id == accid:
                self.accholders.remove(id)
                print('\n----------------------------------------')
                print(f'Account {accid} successfully deleted!!')
                print('----------------------------------------\n')
                return
        print('\n------------------------------')
        print('Account id did\'nt found')  
        print('------------------------------\n')  

#----------------------------------------------------------------

acc1 = Bank('ss')

def account_holder():
    print('\n---------- Create an Account ----------\n')
    name = input('Enter Name: ')
    email = input('Enter Email: ')
    address = input('Enter Address: ')
    acc_type = input('Enter Acoount Type(saving/current): ')
    acc = AccHolder(acc1, name, email, address, acc_type)
    acc.add_acc_holder(acc1)
    while True:
        print('\n-----------------------------')
        print('1. Deposit money')
        print('2. Withdraw money')
        print('3. Check Balance')
        print('4. Transaction History')
        print('5. Take Loan')
        print('6. Transfer money')
        print('7. Exit')
        print('-----------------------------')
        option = int(input('Enter Option: '))
        
        if option == 1:
            amount = int(input('Enter amount to deposit: '))
            acc.deposit(acc1, amount)
        elif option == 2:
            amount = int(input('Enter amount to withdraw: '))
            acc.withdraw(acc1, amount)
        elif option == 3:
            acc.available_balance()
        elif option == 4:
            acc.transaction_history()
        elif option == 5:
            amount = int(input('Enter Amount: '))
            acc.take_loan(acc1, amount)
        elif option == 6:
            amount = int(input('Enter amount to transfer: '))
            id = int(input('Enter id: '))
            acc.transfer_money(acc1, amount, id)
        elif option == 7:
            break
        else:
            print('\n---------------------------------')
            print('Envalid Input, please try again!')
            print('---------------------------------\n')

#---------------------------------------------------------------------

def admin():
    name = input('\nEnter Admin\'s Name: ')
    email = input('Enter Admin\'s Email: ')
    address = input('Enter Admin\'s Address: ')
    ad = Admin(name, email, address)
    
    while True:
        print('\n------------------------------')
        print('1. Create an account as user')
        print('2. See all account list')
        print('3. Delete an account')
        print('4. Total available Bank balance')
        print('5. Total loan amount')
        print('6. Loan Status')
        # ON/OFF Should be capital
        print('7. Turn ON/OFF) loan Status')
        print('8. Bankrupt Status')
        # ON/OFF Should be capital
        print('9. Turn ON/OFF Bankrupt')
        print('10. Exit')
        print('------------------------------')
        option = int(input('Enter Option: '))
        
        if option == 1:
            account_holder()
        elif option == 2:
            ad.show_all_user(acc1)
        elif option == 3:
            id = int(input('Enter an account Id to Delete: '))
            ad.delete_an_account(acc1, id)
        elif option == 4:
            ad.check_total_balance(acc1)
        elif option == 5:
            ad.check_loan_amount(acc1)
        elif option == 6:
            ad.loan_status(acc1)
        elif option == 7:
            status = input('Enter Status (ON/OFF)(in capital): ')
            ad.on_off(acc1, status)
        elif option == 8:
            ad.bankrupt(acc1)
        elif option == 9:
            status = input('Enter Bankrupt Status (ON/OFF)(in capital): ')
            ad.bankrupt_on_off(acc1, status)
        elif option == 10:
            break
        else:
            print('\n---------------------------------')
            print('Envalid Input, please try again!')
            print('---------------------------------\n')

#------------------------------------------------------------------------------
while True:
    print('\n---------- Welcome----------')
    print('1. Account Holder/Owner')
    print('2. Admin')
    print('3. Exit')

    option = int(input('Enter Option: '))

    if option == 1:
        account_holder()
    elif option == 2:
        admin()
    elif option == 3:
        break
    else:
        print('\n---------------------------------')
        print('Envalid Input, please try again!')
        print('---------------------------------\n')