
get_details = int(input('enter the amount\n'))

if get_details < 10:
    print('please donate more')
elif get_details == 10:
    print('please requisting you to donate more than 10 Rs')
else:
    print('thank you ' + str(get_details) + ' Rs was creadited to your account')