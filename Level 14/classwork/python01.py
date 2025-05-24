people = int(input('number of people: '))
time = int(input('your time 1-12: '))
turn = int(input('true or false: '))
lightsOn = people >= 2 and time >= 7 and turn == True 
print('you are hired: ' + str(lightsOn))