print('Welcome to the restaurant')
print('Menu:')

print('1:bennedosa 2:vada 3:poori 4:vadapav 5:coffee 6:misalpav')
user_choice = int(input('Enter your choice: '))

match user_choice:
    case 1:print('You have selected idly')
    case 2:print('You have selected vada')
    case 3:print('You have selected poori')
    case 4:print('You have selected tea')
    case 5: print('You have selected coffee')
    case _:print('Invalid choice, please try again')
