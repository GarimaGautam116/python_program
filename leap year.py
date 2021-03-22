year=int(input('ENTER THE YEAR'))
if year%4==0:
    if year%100!=0:
        print('Leap year')
    else:
        if year%400==0:
            print('leap year')
        else:
            print(' not leap year')

else:
        print('not leap year')
