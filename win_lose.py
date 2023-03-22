from random import randint as one_to_thirty
from decouple import config


def casino():
    my_money = config('MY_MONEY', cast=int)
    balance = my_money
    while True:
        win_slot = one_to_thirty(1, 31)
        chose_slot = int(input('Выберите слот '))
        if chose_slot in range(1, 31):
            print('Слот выбран. Делайте ставку.')
        else:
            print('Выберите слот от 1 до 30')
        bet = int(input('Выберите ставка '))
        if balance < bet:
            print(f'У вас столько денег на балансе. У вас на балансе: {balance}')
        else:
            print('Ставка сделана!')
        if win_slot == chose_slot:
            balance += bet * 2
            print(f'You won ${bet * 2} !!!, Your balance: {balance}')
        elif win_slot != chose_slot:
            balance -= bet
            print(f'Your bet not win. Your balance: {balance}')

        if balance > 0:
            a = input('Do you wanna bet again? Yes/No').lower()
            if a == 'yes':
                continue
            elif a == 'no':
                print(f'Your balance: {balance}')
                break
            else:
                break


if __name__ == '__main__':
    casino()
