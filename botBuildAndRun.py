"""
Code by cameron.albin & christopher.vandervoort
"""

import random

def createBotWeights():
    #A = inputs (42 nodes)
    #B = first hidden layer (16 nodes)
    #C = second hidden layer (16 nodes)
    #D = 7 outputs

    #create list of weights from single node to each node in next layer
    def initializeNode(numOutputs):
        nodeWeights = []
        for x in range(numOutputs):
            nodeWeights += [random.uniform(-1,1)]
        return nodeWeights

    #create list of nodes
    def initializeLayer(numNodes,numOutputs):
        layer = []
        for x in range(numNodes):
            node = initializeNode(numOutputs)
            layer += [node]
        return layer

    #create list of all layers
    ALayer = initializeLayer(42,16)
    BLayer = initializeLayer(16,16)
    CLayer = initializeLayer(16,7)

    botWeights = [ALayer,BLayer,CLayer]
    #access single weight through botWeights[layerNum][nodeNum][nextNodeNum]
    return botWeights

def crossParents(bot1,bot2):
    newBot = []
    for layerNum in range(len(bot1)):
        newLayer = []
        for nodeNum in range(len(bot1[layerNum])):
            newNode = []
            for weightNum in range(len(bot1[layerNum][nodeNum])):
                parentWeights = [bot1[layerNum][nodeNum][weightNum], bot2[layerNum][nodeNum][weightNum]]
                newWeight = random.choice(parentWeights)
                if random.uniform(0,1) <= 0.02:
                    newWeight += random.uniform(-.3,.3)
                newNode += [newWeight]
            newLayer += [newNode]
        newBot += [newLayer]
    return newBot

def runLayer(layerInputs,layer):
    layerOutputs = [0]*len(layer[0])
    for i in range(len(layerInputs)):
        for o in range(len(layerOutputs)):
            layerOutputs[o] += layerInputs[i]*layer[i][o]
    if len(layerOutputs) != 7:
        for o in range(len(layerOutputs)):
            layerOutputs[o] = max(0,layerOutputs[o])
    return layerOutputs

def runBot(boardInput,bot):
    BLayerInputs = runLayer(boardInput,bot[0])
    CLayerInputs = runLayer(BLayerInputs,bot[1])
    boardOutputs = runLayer(CLayerInputs,bot[2])

    sortedOutputs = sorted(boardOutputs,reverse=True)
    columnPreferences = []
    for x in range(len(boardOutputs)):
        pos = boardOutputs.index(sortedOutputs[x])
        columnPreferences.append(pos)
        boardOutputs[pos] = -1000

    return columnPreferences
