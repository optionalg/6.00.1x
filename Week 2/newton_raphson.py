"""
Use Newton-Raphson to find the square root of a number
"""

EPSILON = 0.01
NUMBER = 24.0
GUESS = NUMBER/2.0
NUM_GUESSES = 0

while abs(GUESS*GUESS - NUMBER) >= EPSILON:
    NUM_GUESSES += 1
    GUESS = GUESS - (((GUESS**2) - NUMBER)/(2*GUESS))

print 'number of guesses: ' + str(NUM_GUESSES)
print 'Square root of ' + str(NUMBER) + ' is about ' + str(GUESS)
