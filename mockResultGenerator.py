import random
import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(5):
    with open('test' + str(i)+'.txt', 'w') as file:
        file.write('MD5   Chips  GamesPlayed\n')
        for j in range(5):
            hash = ''.join(random.choice(alphabet) for x in range(32))
            chips = random.randint(1000, 5000)
            gp = random.randint(1, 10)
            file.write(hash + '    ' + str(chips) + '  ' + str(gp) + '\n')

            
