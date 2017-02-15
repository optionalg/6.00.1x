"""
Credit card balance calculator
@author: Andres Rojas
"""

#balance = 42
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

MONTHLY_INTEREST_RATE = annualInterestRate / 12.0

def monthly_payment(current_balance):
    """
    current_balance: number.
    Returns the minimum monthly payment for current balance
    """
    return current_balance * monthlyPaymentRate

def balance_after_payment(current_balance):
    """
    current_balance: number.
    Returns the remaining balance after paying the minimum monthly payment
    """
    return current_balance - monthly_payment(current_balance)

def updated_balance(prev_balance):
    """
    prev_balance: number.
    Returns the balance after payment plus interest
    """
    remaining_balance = balance_after_payment(prev_balance)
    return remaining_balance + (MONTHLY_INTEREST_RATE * remaining_balance)

MONTH = 1

while MONTH <= 12:
    balance = updated_balance(balance)
    #print 'Month' + str(MONTH) + ' Remaining balance:' + str(balance)
    MONTH += 1

ROUNDED_BALANCE = round(balance, 2)

print('Remaining balance: ' + str(ROUNDED_BALANCE))
