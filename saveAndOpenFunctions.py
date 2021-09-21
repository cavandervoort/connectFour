# -*- coding: utf-8 -*-
"""
Wuts up on dem dizates y'all? Mon Sep 20 15:34:15 2021

@Who dat bad man programmin? cameron.albin
"""


#Saving File
import pickle
output = open('childBot.pkl','wb')
pickle.dump(childBot, output)
output.close()

#Opening Bot
import pickle
pkl_file = open('C:\\Users\\cameron.albin\\.spyder-py3\\Connect4\\childBot.pkl', 'rb')
data1 = pickle.load(pkl_file)
print(data1[0][0])
pkl_file.close()


