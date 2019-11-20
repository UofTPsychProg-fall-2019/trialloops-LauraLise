#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""

#%% Required set up 

import numpy as np
import pandas as pd
import os, sys
import random
from psychopy import visual, core, event, gui, logging


#%% identify who the data belongs to 

# show the dialog box, create a field for subject ID and session number
subgui = gui.Dlg()
subgui.addField("Subject ID:")
subgui.addField("Session Number:")

# show the gui
subgui.show()

# put the inputted data in easy to use variables
subjID = subgui.data[0]
sessNum = subgui.data[1]

# if the file name already exists, give a notification and exit out of the experiment
ouputFileName = 'sub'+subjID+'_'+'sess'+sessNum+'.csv'
if os.path.isfile(ouputFileName) :
    sys.exit("data for this session already exists")



#%% set up study  

# pressing q will quit 
event.globalKeys.add(key='q', func=core.quit)

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# a list called "stim" that contains trial-specific info (stimulus, etc)
stim = ['A','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','W','X','Y','Z']

# randomly shuffle the stimuli so the order is no predictable 
random.shuffle(stim)

#define the number of stimuli
nstim = len(stim)

# define the count
myCount = 0

# create empty lists, which will be used to store the button responses, stimuli presented, and trial number
response_to_save = []
stim_to_save = []
trialnum_to_save = []


#%% my loop here

# task instructions before starting the loop 

instructions = visual.ImageStim(win, image='instructions.jpg', pos=(0,0), size=(1.5,1.5)) 
instructions.draw()
win.flip()
event.waitKeys(keyList=['f'])

#%% my loop here

for trial in range(nstim): 
    myCount += 1 # keep track of the trial number 
    thisStimName = stim[trial] # index the items in the stimulus list 
    
    # define the stimuli and text to use for the experiment 
    thisStim = visual.ImageStim(win, image='letters'+'/'+ thisStimName + '.jpg', pos=(0,0), size=(1.5,1.5)) # give path to stimulus (using thisStimName)
    myTextquestion = visual.TextStim(win, text="Was this letter on the study list?", pos = (0,0.5), color="black") 
    myTextF = visual.TextStim(win, text="f = yes", pos = (-0.25,-0.5), color="black") 
    myTextJ = visual.TextStim(win, text="j = no", pos = (0.25,-0.5), color="black") 
    fixation = visual.TextStim(win, text="+", color="black")
    
    # draw the text and the stimulus 
    thisStim.draw() 
    myTextquestion.draw()
    myTextF.draw()
    myTextJ.draw()
    
    # flip it
    win.flip()
    
    # define which keys are valid responses and the max time the stimulus will be shown
    keys = event.waitKeys(keyList=['f','j'],maxWait=(3))
    
    # save the responses, stimuli shown, and trial number in a numpy array
    response_to_save = np.append(response_to_save, keys)
    stim_to_save = np.append(stim_to_save, thisStimName)
    trialnum_to_save = np.append(trialnum_to_save, myCount)
    
    # show a fixation after each letter stimulus 
    fixation.draw()
    win.flip()
    
    # clear the events
    event.clearEvents() 

core.wait(1)
win.close()



#%% save the data into a csv file 

# Create a dictionary with the data
data = {'Stimulus': stim_to_save, 
        'Response': response_to_save, 
        'Trial': trialnum_to_save} 
  
# Convert the dictionary into a pandas DataFrame 
out = pd.DataFrame(data) 

# Save the pandas DataFrame into a csv file, which is named after the subject ID and session number
out.to_csv('sub'+subjID+'_'+'sess'+sessNum+'.csv', index = False)

