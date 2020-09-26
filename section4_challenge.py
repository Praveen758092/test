print('Please choose any of the options below')

choice='-'

while True:
    if choice=='1':
        break
    elif choice in '1234':
        print('you have choosen {}'.format(choice))
    else:
        print('1.one')
        print('2.two')
        print('3.three')
        print('4.four')

    choice=input()



