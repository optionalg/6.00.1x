"""
Calculates the minimum fixed monthly payment needed in
order pay off a credit card balance within 12 months
@author: Andres Rojas
"""

#balance = 3329
#annualInterestRate = 0.2

#balance = 4773
#annualInterestRate = 0.2

balance = 3926
annualInterestRate = 0.2

CALCULATED_BALANCE = balance
FIXED_PAYMENT = 0
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

while CALCULATED_BALANCE > 0:
    CALCULATED_BALANCE = balance
    FIXED_PAYMENT += 10
    MONTH = 1
    while MONTH <= 12:
        CALCULATED_BALANCE = updated_balance(CALCULATED_BALANCE, FIXED_PAYMENT)
        MONTH += 1

print 'Lowest Payment: ' + str(FIXED_PAYMENT)
