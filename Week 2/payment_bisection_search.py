"""
Calculates the minimum fixed monthly payment needed in
order pay off a credit card balance within 12 months
@author: Andres Rojas
"""

#balance = 320000
#annualInterestRate = 0.2

balance = 999999
annualInterestRate = 0.18

MONTHLY_INTEREST_RATE = annualInterestRate / 12.0

def balance_after_payment(prev_balance, payment):
    """
    prev_balance: number.
    payment: number.
    Returns the remaining balance after paying a fixed payment
    """
    return prev_balance - payment

def updated_balance(prev_balance, payment):
    """
    prev_balance: number.
    payment: number.
    Returns the balance after payment plus interest
    """
    unpaid_balance = balance_after_payment(prev_balance, payment)
    return unpaid_balance + (MONTHLY_INTEREST_RATE * unpaid_balance)

CALCULATED_BALANCE = balance
FIXED_PAYMENT = balance / 12
LOWER_BOUND = 0
UPPER_BOUND = (balance * ((1 + MONTHLY_INTEREST_RATE)**12)) / 12.0

while abs(CALCULATED_BALANCE) > 0.1:
    if CALCULATED_BALANCE > 0:
        LOWER_BOUND = FIXED_PAYMENT
    else:
        UPPER_BOUND = FIXED_PAYMENT

    CALCULATED_BALANCE = balance
    FIXED_PAYMENT = (UPPER_BOUND + LOWER_BOUND) / 2.0
    MONTH = 1

    while MONTH <= 12:
        CALCULATED_BALANCE = updated_balance(CALCULATED_BALANCE, FIXED_PAYMENT)
        MONTH += 1

LOWEST_PAYMENT = round(FIXED_PAYMENT, 2)

print 'Lowest Payment: ' + str(LOWEST_PAYMENT)
