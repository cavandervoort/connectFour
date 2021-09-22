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
    
    #create list of layer biases
    def initializeBiases(numNodes):
        layerBiases = []
        for x in range(numNodes):
            layerBiases += [random.uniform(-1,1)]
        return layerBiases
        
    #create list of all layers
    AtoBLayer = initializeLayer(42,16)
    BtoCLayer = initializeLayer(16,16)
    CtoDLayer = initializeLayer(16,7)
    BLayerBiases = initializeBiases(16)
    CLayerBiases = initializeBiases(16)
    DLayerBiases = initializeBiases(7)

    botWeights = [AtoBLayer,BtoCLayer,CtoDLayer,BLayerBiases,CLayerBiases,DLayerBiases]
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

def layerOutputToNextLayerInput(layerOutputs,layer):
    nextLayerInputs = [0]*len(layer[0])
    for o in range(len(layerOutputs)):
        for i in range(len(nextLayerInputs)):
            nextLayerInputs[i] += layerOutputs[o]*layer[o][i]
#    if len(nextLayerInputs) != 7:
#        for i in range(len(nextlayerInputs)):
#            nextlayerInputs[i] = max(0,nextlayerInputs[i])
    return nextLayerInputs

def layerInputToLayerOutput(layerInputs,layerBiases):
    for i in range(len(layerInputs)):
        layerInputs[i] += layerBiases[i]
        if len(layerBiases) != 7:
            layerInputs[i] = max(0,layerInputs[i])
    layerOutputs = layerInputs
    return layerOutputs            

def runBot(boardInput,bot):
    BLayerInputs = layerOutputToNextLayerInput(boardInput,bot[0])
    BLayerOutputs = layerInputToLayerOutput(BLayerInputs,bot[3])   
    CLayerInputs = layerOutputToNextLayerInput(BLayerOutputs,bot[1])
    CLayerOutputs = layerInputToLayerOutput(CLayerInputs,bot[4])   
    DLayerInputs = layerOutputToNextLayerInput(CLayerOutputs,bot[2])
    boardOutputs = layerInputToLayerOutput(DLayerInputs,bot[5])

    sortedOutputs = sorted(boardOutputs,reverse=True)
    columnPreferences = []
    for x in range(len(boardOutputs)):
        pos = boardOutputs.index(sortedOutputs[x])
        columnPreferences.append(pos)
        boardOutputs[pos] = -1000

    return columnPreferences


#boardInput = []
#for x in range(42):
#    boardInput += [random.choice([0])]
#bot = createBotWeights()
#runBot(boardInput,bot)





