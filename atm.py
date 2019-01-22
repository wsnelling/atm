"""
This is a program that asks the user for their PIN number.
The valid PIN number is "1234".
The user has 3 attempts to enter the correct pin until they are
locked out of their account. If the correct value is entered, a message
is printed and the program ends. Note that there is no fixed input/output
"""
from colorama import Fore, Back, Style, init
init()
init(autoreset=True)
def main():
    """
    This is the main function section of the PIN validation program.
    """
    print('Welcome to the ATM PIN validation program')
    valid_pin = 1234
    pin_tries = 1
    while True:
        #prompt the user to enter their PIN number
        pin = input("Please enter your 4 digit PIN number: ")
        if not pin:
            print(
                Fore.LIGHTWHITE_EX + Back.RED +
                'You have failed to enter any PIN, try again'
                )
            print('\a')
        elif pin == str(valid_pin):
            print(
                Fore.BLUE + Style.BRIGHT + Back.LIGHTYELLOW_EX
                +'Your account balance is: $0.00.  Goodbye!'
                )
            break
        elif pin_tries > 2:
            print(
                Fore.YELLOW + Style.BRIGHT + Back.RED +
                'Account locked. THE POLICE ARE ON THEIR WAY!'
                )
            print('\a\a\a\a\a\a\a\a\a')
            break
        else:
            pin_tries += 1
            print(Fore.YELLOW + Style.BRIGHT + Back.RED +'Invalid pin. ')

if __name__ == '__main__':
    main()
