import argparse
from math import ceil, log
from utils import Validator


def annuity(args_):
    principal = int(args_.principal)
    periods = int(args_.periods)
    interest = int(args_.interest)
    i = interest / (12 * 100)
    payment = principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
    print(f"Your monthly payment = {ceil(payment)}!")
    print(f'Overpayment {ceil(payment) * ceil(periods) - principal}')


def load_principal(args_):
    payment = int(args_.payments)
    periods = int(args_.periods)
    interest = int(args_.interest)
    i = interest / (12 * 100)
    principal = payment * ((1 + i) ** periods - 1) / (i * (1 + i) ** periods)
    print(f"Your loan principal = {round(principal)}!")
    print(f'Overpayment {ceil(payment) * ceil(periods) - principal}')


def monthly(args_):
    principal = int(args_.principal)
    payment = int(args_.payments)
    interest = int(args_.interest)
    i = interest / (12 * 100)
    months = log((payment / (payment - i * principal)), 1 + i)
    years = round(months / 12)
    months_left = months % 12
    if years == 0:
        print(f"It will take {ceil(months_left)} months to repay this loan!")
    elif years >= 1 and months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {ceil(months_left)} months to repay this loan!")
    print(f'Overpayment {ceil(payment) * ceil(months) - principal}')


def diff(args_):
    principal = int(args_.principal)
    periods = int(args_.periods)
    interest = int(args_.interest)
    i = interest / (12 * 100)
    payment_differentiation = [ceil(principal / periods + i * (principal - (principal * (k - 1) / periods)))
                               for k in range(1, periods + 1)]
    overpayment = 0
    for month, payment in enumerate(payment_differentiation):
        print(f'Month {month + 1}: payment is {payment}!')
        overpayment += payment
    print(f'Overpayment {overpayment - principal}')


def credit_calculator(args_):
    calculate = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal
type "d" for calculation of differentials: """)

    if calculate == "n":
        monthly(args_)
    elif calculate == "a":
        annuity(args_)
    elif calculate == "p":
        load_principal(args_)
    elif calculate == "d":
        diff(args_)
    else:
        print("Wrong type!")
        exit(255)

    # print(args_)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="type")
    parser.add_argument("-i", "--interest", help="interest", type=float)
    parser.add_argument("-pay", "--payments", help="payment", type=int)
    parser.add_argument("-pr", "--principal", help="principal", type=float)
    parser.add_argument("-pe", "--periods", help="periods", type=float)
    args = parser.parse_args()

    validator = Validator(parser.parse_args())
    # result = validator._validate()
    credit_calculator(args_=args)
    # credit_calculator(result)
