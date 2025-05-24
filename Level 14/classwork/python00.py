age = int(input('your age: '))
expirience = int(input('your experience: '))
height = int (input('your height: '))
IsHired = age >= 18 and expirience >= 1 and height >= 175
print('you are hired: ' + str(IsHired))
