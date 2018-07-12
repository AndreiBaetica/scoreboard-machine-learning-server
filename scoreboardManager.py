import sys
import os
import re
from operator import itemgetter

def dirToDict(dir):

    finalList = []
    #extracting data
    for filename in os.listdir(dir):
        with open(dir + '/' + filename) as file:
            next(file)
            dictList = []
            for line in file:
                line = re.sub(' +',' ', line)
                data = line.split()
                print(line)
                dictList.append({'hash' : data[0], 'chips' : data[1], 'gamesPlayed' : data[2]})
            #sorting, assigning score
            dictList = sorted(dictList, key=itemgetter('chips'), reverse=True)
            score = 120
            for dict in dictList:
                if score >= 20:
                    score -= 20
                dict['points'] = score + 10
            finalList.append(dictList)
            

if __name__ == '__main__':

    dir = sys.argv[1]

    dirToDict(dir)




