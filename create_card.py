import random
new_card = None
new_pin = None
card_checksum = None
logined = False
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
def create_card():
    global new_card
    card_iin = 400000
    card_id = random.randint(100000000,999999999)
    new_card = str(card_iin) + str(card_id)
    card_checksum = luhn_algorithm()
    new_card = new_card + str(card_checksum)
    print(f'''
Your card has been created
Your card number:
{new_card}''')
    return new_card
def create_pin():
    new_pin = str(random.randint(1000,9999))
    print(f'''Your card PIN:
{new_pin}
    ''')
    return new_pin
def login():
    ent_card_number = str(input('Enter your card number:'))
    ent_pin = str(input("Enter your PIN:"))
    while ent_card_number != new_card or ent_pin != new_pin:
        print("Wrong card number or PIN!")
        break
    else:
        print("You have successfully logged in!")
        global logined
        logined = True

def luhn_algorithm():
    global card_checksum
    sum = 0
    luhn = new_card[:]
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
        print(sum)
        card_checksum = 0
        return card_checksum
    else:
        for i in range(0,10):
            if (sum + i) % 10 == 0:
                card_checksum = i
                return i

if __name__ == '__main__':
    menu_one()
    choice = int(input())
    while choice in (1, 2):
        if choice == 1 and logined == False:
            new_card = create_card()
            new_pin = create_pin()
            menu_one()
            choice = int(input())
        elif choice == 2:
            login()
            if logined == False:
                menu_one()
                choice = int(input())
                continue
            menu_two()
            choice = int(input())
            if choice in (1, 2):
                while choice == 1:
                    balance = 0
                    print("Balance: {0}".format(balance))
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

