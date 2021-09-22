# -*- coding: utf-8 -*-
"""
Wuts up on dem dizates y'all? Mon Sep 20 15:34:15 2021

@Who dat bad man programmin? cameron.albin
"""
import pickle

def saveBots(bots,fileName):
    output = open(fileName,'wb')
    pickle.dump(bots, output)
    output.close()

def loadBots(fileName):
    pkl_file = open(fileName, 'rb')
    data1 = pickle.load(pkl_file)
    pkl_file.close()
    return data1

