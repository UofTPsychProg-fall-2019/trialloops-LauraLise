#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# pressing 'q' will quit 
event.globalKeys.add(key='q', func=core.quit)

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()

#%% up to you!
# this is where you build a trial that you might actually use one day!
# just try to make one trial ordering your lines of code according to the 
# sequence of events that happen on one trial
# if you're stuck you can use the responseExercise.py answer as a starting point 

# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))  

LetterA = visual.ImageStim(win, image=r'letters\A.jpg', pos=(0,0), size=(2,2))

#myText = ... #note default color is white, which you can't see on a white screen!
myTextquestion = visual.TextStim(win, text="Was this letter on the study list?", pos = (0,0.5), color="black")
myTextF = visual.TextStim(win, text="f = yes", pos = (-0.25,-0.5), color="black")
myTextJ = visual.TextStim(win, text="j = no", pos = (0.25,-0.5), color="black")

# then draw all stimuli
LetterA.draw()
myTextquestion.draw()
myTextF.draw()
myTextJ.draw()

# then flip your window
win.flip()

# then record your responses
keys = event.waitKeys(keyList=['f','j'], maxWait=(3))
print(keys)

# present the fixation cross after the stimulus
fixation = visual.TextStim(win, text="+", pos = (0,0),color="black")
fixation.draw()
win.flip()

#% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly
core.wait(2)
win.close()
