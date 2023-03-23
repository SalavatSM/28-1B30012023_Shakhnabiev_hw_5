from random import randint as one_to_thirty
from decouple import config


def casino():
    my_money = config('MY_MONEY', cast=int)
    balance = my_money
    while balance > 0:
        win_slot = one_to_thirty(1, 31)
        chose_slot = int(input('Select your slot between 1 and 30\n'))
        while chose_slot > 30 or chose_slot < 1:
            print('It does not have slot with such a number.')
            chose_slot = int(input('Select slot between 1 and 30\n'))
        else:
            print(f'Slot number {chose_slot} selected')
        bet = int(input('Place your bet!\n'))
        while bet > balance:
            print(f'You do not have enough money to bet so much money. Your balance is: {balance}')
            print('Place your bet not much than your balance.')
            bet = int(input('Place your bet!\n'))
        else:
            print('Bet is placed!')
        if win_slot == chose_slot:
            balance += bet * 2
            print(f'Your bet has won!!!\nYou won ${bet * 2} !!!\nYour balance: {balance}')
        elif win_slot != chose_slot:
            balance -= bet
            print(f'Your bet is not win. Your balance: {balance}')

        if balance > 0:
            answer = input('Do you wanna keep playing? Yes/No\n').lower()
            while answer != 'Yes'.lower() and answer != 'No'.lower():
                answer = input('Do you wanna keep playing? Yes/No\n').lower()
            else:
                if answer == 'Yes'.lower():
                    continue
                elif answer == 'No'.lower():
                    print(f'Your balance: {balance}.\nGlad to see you again!')
                    break
    else:
        print('We are glad to see you again with your money!')


if __name__ == '__main__':
    casino()
