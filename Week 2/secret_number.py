print('Please think of a number between 0 and 100!')

low = 0
high = 100
ans = (high - low) // 2

while True:
    print('Is you secret number ' + str(ans) + '?')
    command = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if command == 'h':
        high = ans
    elif command == 'l':
        low = ans
    elif command == 'c':
        print('Game over. Your secret number was: ' + str(ans))
        break
    else:
        print('Sorry, I did not understand your input.')

    ans = ((high - low) // 2) + low
