import random
class CreateCard:
    def __init__(self):
        self.card_number = self.create_card()
        self.pin = self.create_pin()
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
            for i in range(0,10):
                if (sum + i) % 10 == 0:
                    self.card_checksum = i
                    return self.card_checksum

logined = False
class Login:
    def __init__(self):
        self.login = self.login()
    def login(self):
        global card_number
        global card_pin
        global logined
        ent_card_number = str(input("Enter your card number:"))
        ent_pin = str(input("Enter your PIN:"))
        while ent_card_number != card_number or ent_pin != card_pin:
            print("Wrong card number or PIN!")
            break
        else:
            print("You have successfully logged in!")
            logined = True
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
            menu_two()
            choice = int(input())
            if choice in (1, 2):
                while choice == 1:
                    balance = 0
                    print(f"Balance: {balance}")
                    menu_two()
                    choice = int(input())
                    continue
                if choice == 2:
                    print("You have successfully logged out!")
                    menu_one()
                    choice = int(input())
                    logined = False
                    continue
                else:
                    break
            break
            print("Bye!")
        else:
            break
    print("Bye!")
