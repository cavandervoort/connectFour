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


def runLayer(layerInputs,layer):
    layerOutputs = [0]*len(layer[0])
    for i in range(len(layerInputs)):
        for o in range(len(layerOutputs)):
            layerOutputs[o] += layerInputs[i]*layer[i][o]
    return layerOutputs

def runBot(boardInput,bot):
    layer = bot[0]
    BLayerInputs = runLayer(boardInput,layer)
    layer = bot[1]
    CLayerInputs = runLayer(BLayerInputs,layer)
    layer = bot[2]
    boardOutputs = runLayer(CLayerInputs,layer)

    sortedOutputs = sorted(boardOutputs,reverse=True)
    columnPreferences = []
    for x in range(len(boardOutputs)):
        columnPreferences += [boardOutputs.index(sortedOutputs[x])]

    return columnPreferences
