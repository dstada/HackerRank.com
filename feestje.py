import datetime


def print_header():
    print('--------------------------------------------')
    print('       BIRTHDAY APP')
    print('--------------------------------------------')
    print()


# Input:
def user_input():
    print('Wanneer ben je geboren? ')
    day = int(input('Dag [DD]: '))
    month = int(input('Maand [MM]: '))
    year = int(input('Jaar [JJJJ]: '))
    birthday = datetime.datetime(year, month, day)
    print(birthday)
    return birthday

# Give results:
# Aantal dagen in leven:
def days():
    print("Hier dagen geven")

# Verjaardag over x dagen:
def birthday():
    print("Hier verjaardag")


def main():
    print_header()
    user_input()
    days()
    birthday()

main()
