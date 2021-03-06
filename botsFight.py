import botBuildAndRun
import playConnectFourBotsOnly
import random
import saveAndOpenFunctions

def buildBots(numBots):
    bots = []
    for _ in range(numBots):
        bots.append(botBuildAndRun.createBotWeights())
    return bots

def fightAndSortBots(bots):
    numBots = len(bots)
    winCount = [[0,x] for x in range(numBots)]

    for diff in range(1,numBots//2+1):
        for botAPos in range(numBots):
            botA = bots[botAPos]
            botBPos = (botAPos+diff) % numBots
            botB = bots[botBPos]
            winner = playConnectFourBotsOnly.playGameBots(botA,botB,False)
            if winner == 1:
                winCount[botAPos][0] += 1
            else:
                winCount[botBPos][0] += 1

    winCount.sort()
    winCount.reverse()

    sortedBots = []
    for score,pos in winCount:
        sortedBots.append(bots[pos])

    return sortedBots

def buildNextGenBots(parentBots,numBots):
    newBots = []
    numParents = len(parentBots)
    while len(newBots) < (numBots - numParents):
        botA = parentBots[random.randint(0, numParents-1)]
        botB = parentBots[random.randint(0, numParents-1)]
        newBots.append(botBuildAndRun.crossParents(botA,botB))

    return parentBots + newBots

def printAFight(botA,botB,day):
    print(f"\nhere is a sample fight from day {day}:\n")
    playConnectFourBotsOnly.playGameBots(botA,botB,True)

import time
start = time.time()

numBots = 100

bots = buildBots(numBots) #if building new set of bots
#bots = saveAndOpenFunctions.loadBots('savedBots.pkl') #if saving past bots
print(f'built bots in {time.time() - start} seconds')

days = 2
for day in range(days):
    if day % 1 == 0:
        printAFight(bots[0],bots[1],day)
        print(f'Day {day} starting at {time.time() - start} seconds')
    parentBots = fightAndSortBots(bots)[:numBots//10]
    bots = buildNextGenBots(parentBots,numBots)

print("DONE")
#saveAndOpenFunctions.saveBots(bots,'savedBots.pkl') #if want to save bots



#
