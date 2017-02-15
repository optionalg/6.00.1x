"""
Convert decimal fraction into binary number
"""

DECIMAL_NUMBER = float(input('Enter a decimal number: '))
POWER = 0
ITERATIONS = 0

while ((2**POWER)*DECIMAL_NUMBER)%1 != 0:
    POWER += 1
    ITERATIONS += 1

INTEGER_NUMBER = int(DECIMAL_NUMBER*(2**POWER))

RESULT = ''

if INTEGER_NUMBER == 0:
    RESULT = '0'
while INTEGER_NUMBER > 0:
    RESULT = str(INTEGER_NUMBER%2) + RESULT
    INTEGER_NUMBER = INTEGER_NUMBER//2

for i in range(POWER - len(RESULT)):
    RESULT = '0' + RESULT

RESULT = RESULT[0:-POWER] + '.' + RESULT[-POWER:]
print 'The binary representation of the decimal ' + str(DECIMAL_NUMBER) + ' is ' + RESULT
print 'Iterations required ' + str(ITERATIONS)
