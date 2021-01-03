import random
import sqlite3

logined = False
card_number = None
class CreateCard:
    def __init__(self):
        self.database = self.create_database()
        self.card_number = self.create_card()
        self.pin = self.create_pin()
        self.add_pin_number = self.add_pin_number()

    def create_database(self):
        self.connect = sqlite3.connect("card.s3db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS card
        (id INTEGER,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0);
        """)
        self.connect.commit()

    def create_card(self):
        card_iin = 400000
        card_id = random.randint(00000000, 999999999)
        self.card_number = str(card_iin) + str(card_id)
        self.card_checksum = self.luhn_algorithm()
        self.card_number += str(self.card_checksum)
        print(f'''
Your card has been created
Your card number:
{self.card_number}''')
        return self.card_number

    def create_pin(self):
        self.pin = str(random.randint(1000, 9999))
        print(f'''
Your card PIN:
{self.pin}
            ''')
        return self.pin

    def add_pin_number(self):
        self.cursor.execute("INSERT INTO card VALUES (?, ?, ?, ?)", (1, self.card_number, self.pin, 0))
        self.connect.commit()

    def luhn_algorithm(self):
        sum = 0
        luhn = self.card_number[:]
        for index, value in enumerate(luhn):
            n = int(value)
            if (index + 1) % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
                sum += n
            else:
                sum += n
        if sum % 10 == 0:
            card_checksum = 0
            return card_checksum
        else:
            for i in range(0, 10):
                if (sum + i) % 10 == 0:
                    self.card_checksum = i
                    return self.card_checksum


class Login:
    def __init__(self):
        self.login = self.login()

    def login(self):
        global logined
        global card_number
        ent_card_number = str(input("Enter your card number:"))
        ent_pin = str(input("Enter your PIN:"))
        self.connect = sqlite3.connect("card.s3db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT * FROM card WHERE number = ? AND pin = ?", (ent_card_number, ent_pin))
        if self.cursor.fetchall():
            print("You have successfully logged in!")
            logined = True
            card_number = ent_card_number
        else:
            print("Wrong card number or PIN!")

class Balance:
    def __init__(self):
        self.show_balance()
    def show_balance(self):
        self.connect = sqlite3.connect("card.s3db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT balance FROM card WHERE number = ?", (card_number,))
        self.balance = self.cursor.fetchone()
        for i in self.balance:
            balance = i
            return balance
    def income_balance(self):
        self.connect = sqlite3.connect("card.s3db")
        self.cursor = self.connect.cursor()
        income = int(input())
        self.cursor.execute("SELECT balance FROM card WHERE number = ?", (card_number,))
        balance = self.cursor.fetchone()
        for i in balance:
            balance = i
            print(balance)
        balance += income
        self.cursor.execute("UPDATE card SET balance = ? WHERE number = ?", (balance, card_number))
        self.connect.commit()
        print("Income was added!")
        return balance
    def balance_transfer(self):
        self.connect = sqlite3.connect("card.s3db")
        self.cursor = self.connect.cursor()
        ent_card = int(input("Enter card number:\n"))
        self.cursor.execute("SELECT number FROM card WHERE number = ?", (ent_card,))
        if self.cursor.fetchall():
            ent_amount = int(input("Enter how much money you want to transfer:\n"))
            self.cursor.execute("SELECT balance FROM card WHERE number = ?", (card_number,))
            balance = self.cursor.fetchone()
            for i in balance:
                balance = i
            int(balance)
            if ent_amount > balance:
                print("Not enough money!")
            else:
                self.cursor.execute("SELECT balance FROM card WHERE number = ?", (ent_card,))
                ent_new_balance = self.cursor.fetchone()
                for i in ent_new_balance:
                    ent_new_balance = i
                ent_new_balance += ent_amount
                self.cursor.execute("UPDATE card SET balance = ? WHERE number = ?", (ent_new_balance, ent_card))
                self.connect.commit()
                new_balance = balance - ent_amount
                self.cursor.execute("UPDATE card SET balance = ? WHERE number = ?", (new_balance, card_number))
                self.connect.commit()
                print("Success!")
        else:
            print("Probably you made a mistake in the card number. Please try again!")
    def close_account(self):
        self.connect = sqlite3.connect("card.s3db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("DELETE FROM card WHERE number = ? ", (card_number,))
        self.connect.commit()
        print("The account has been closed!")
if __name__ == '__main__':
    def menu_one():
        print('''
1. Create an account
2. Log into account
0. Exit
    ''')


    def menu_two():
        print(''' 
1. Balance
2. Log out
0. Exit
        ''')
    def menu_three():
        print("""
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit    
""")


    menu_one()
    choice = int(input())
    while choice in (1, 2):
        if choice == 1 and logined == False:
            card = CreateCard()
            card_number = card.card_number
            card_pin = card.pin
            menu_one()
            choice = int(input())
        elif choice == 2:
            login = Login()
            if logined == False:
                menu_one()
                choice = int(input())
                continue
            menu_three()
            choice = int(input())
            while choice in (1, 2, 3, 4):

                while choice == 1:
                    show = Balance
                    print(f"Balance: {show.show_balance(show)}")
                    menu_three()
                    choice = int(input())
                while choice == 2:
                    #bakiye ekleme
                    income = Balance
                    income.income_balance(income)
                    menu_three()
                    choice = int(input())
                    continue
                while choice == 3:
                    transfer = Balance
                    transfer.balance_transfer(transfer)
                    menu_three()
                    choice = int(input())
                    continue
                if choice == 4:
                    close = Balance
                    close.close_account(close)
                    logined = False
                    break
            menu_one()
            choice = int(input())
        else:
            break
    print("Bye!")
