import sys
import os
import re
from operator import itemgetter
import json

def notInCombined(dict, lst):
    for i in lst:
        if i['hash'] == dict['hash']:
            return False
    return True
    
def dictCombiner(lst):
    combinedList = []
    for sublist in lst:
        for i in sublist:
            if notInCombined(i, combinedList):
                combinedList.append(i)
            else:
                for j in combinedList:
                    if j['hash'] == i['hash']:
                        j['points'] += i['points']
                        j['gamesPlayed'] += i['gamesPlayed']
    combinedList = sorted(combinedList, key=itemgetter('points'), reverse=True)        
    return combinedList


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
                dictList.append({'hash' : data[0], 'chips' : data[1], 'gamesPlayed' : data[2]})
            #sorting, assigning score
            dictList = sorted(dictList, key=itemgetter('chips'), reverse=True)
            score = 120
            for dict in dictList:
                if score >= 20:
                    score -= 20
                dict['points'] = score + 10
                dict.pop('chips', None)
                for i in whitelist:
                    if (i['hash'] == dict['hash']) & (int(filename[0]) >= i['day']):
                        dict['points'] = dict['points'] * 2
            finalList.append(dictList)
    return finalList

if __name__ == '__main__':

    
    dir = sys.argv[1]

    #teams that have shared code go here. Add as dicts: {'hash' : '<hash>', 'day' : <int>}
    whitelist = []
    
    scoreList = dictCombiner(dirToDict(dir))
    #scoreList = json.dumps(test)

    with open('scoreboard.html', 'w') as file:
        file.write('<table > <table border="1"> <tbody>')
        file.write('<tr> <td> Team </td> <td> Hash </td> <td> Score </td> </tr>')
        for team in scoreList:
            file.write('<tr> <td> NamePlaceholder </td> <td>' + team['hash'] + '</td> <td>' + str(team['points']) + '</td> </tr>')
        file.write('</tbody> </table>')
            


