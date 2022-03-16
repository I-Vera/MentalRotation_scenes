#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 16, 2022, at 10:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'MentalRotationFinal'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\paper\\Desktop\\PsychoPy\\mentalrotationfinal-master\\mentalrotationfinal-master\\MRF2Pilot_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Hello"
HelloClock = core.Clock()
helloText = visual.TextStim(win=win, name='helloText',
    text='Дорогой испытуемый! \n\nМы изучаем особенности пространственного мышления и хотим выяснить, как люди представляют людей и объекты под разными углами. В данном эксперименте вам предстоит увидеть ряд изображений и после каждого ответить на поставленные вопросы. \nПеред началом вы увидите подробную инструкцию и пример задачи. \n\nЧтобы продолжить, нажмите ПРОБЕЛ.',
    font='Arial',
    units='height', pos=[0, 0], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
helloKey = keyboard.Keyboard()

# Initialize components for Routine "InstructionMR"
InstructionMRClock = core.Clock()
InstMR_text = visual.TextStim(win=win, name='InstMR_text',
    text='Вы увидите ряд изображений, на которых человек сидит за столом. Перед человеком в центре стола расположен прямоугольный планшет, и вокруг планшета расположены 4 точки справа, слева, спереди и сзади.\n\nПри показе изображения одна из точек будет загораться. Под изображением вам также будет схематично представлен пример зажигания точек.\n\nВашей задачей будет определить, СОВПАДАЕТ ЛИ ситуация на изображении с представленным примером.\n\nЕсли изображение и пример РАЗЛИЧАЮТСЯ, нажмите клавишу "<=”. Если они ОДИНАКОВЫЕ, нажмите клавишу “=>”.\n\nДля продолжения нажмите ПРОБЕЛ.',
    font='Arial',
    pos=(0, -0.25), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
InstMR_keyresp = keyboard.Keyboard()
InstMR_image = visual.ImageStim(
    win=win,
    name='InstMR_image', units='height', 
    image='rot60drwhoL.jpg', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
InstMR_stimulus = visual.ImageStim(
    win=win,
    name='InstMR_stimulus', units='height', 
    image='stimuliLeft.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.08, 0.03),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "InstructionQnA"
InstructionQnAClock = core.Clock()
InstQnA_text = visual.TextStim(win=win, name='InstQnA_text',
    text='После ответа на изображения вам нужно оценить, как вы решали задачу. В основном есть 2 типа решения задач: либо через мысленное "поворачивание объектов" до тех пор, пока не получится произвести сравнение, либо через "представление чужой точки зрения" и того, слева или справа по отношению к смотрящему находится зажженая точка.\n\nЕсли в задаче до вопроса вы определили сходство или различие, мысленно поворачивая объекты на столе до нужного угла, нажмите клавишу "<=”.\nЕсли вы определили сходство или различие, представляя себя на чужом месте, нажмите клавишу "=>”. \nЕсли ни один из вариантов не кажется правильным, нажмите клавишу "пробел".\n\nДалее вы потренируетесь на нескольких примерах. Если вы ознакомились с инструкцией, нажмите ПРОБЕЛ.\n',
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
InstQnA_keyresp = keyboard.Keyboard()

# Initialize components for Routine "InstTest"
InstTestClock = core.Clock()
InstTest_text = visual.TextStim(win=win, name='InstTest_text',
    text='Перед основной частью эксперимента вы потренируетесь на 4 задачах. Результаты этих задач не будут учитываться.\nВам понадобятся клавиши: "<=", "=>", "пробел".\n\nНе торопитесь, убедитесь, что вы полностью понимаете, что вам нужно делать. Если у вас возникают вопросы, задавайте их экспериментатору.\n\nЕсли готовы приступить, нажмите ПРОБЕЛ.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
InstTest_keyresp = keyboard.Keyboard()

# Initialize components for Routine "TestTrialMR"
TestTrialMRClock = core.Clock()
TestTrialMR_keyresp = keyboard.Keyboard()
TestTrialMR_stimulus = visual.ImageStim(
    win=win,
    name='TestTrialMR_stimulus', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.27), size=(0.08, 0.03),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
TestTrialMR_image = visual.ImageStim(
    win=win,
    name='TestTrialMR_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.7, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
TestTrialMR_text = visual.TextStim(win=win, name='TestTrialMR_text',
    text="нажмите '<=' для ДРУГОЕ         нажмите '=>' для ТО ЖЕ",
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
polygon_centr = visual.ShapeStim(
    win=win, name='polygon_centr', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "TestTrialQnA"
TestTrialQnAClock = core.Clock()
TestTrialQnA_text = visual.TextStim(win=win, name='TestTrialQnA_text',
    text='Как вы решали?\n\n\n<= поворачивая объекты                представляя точку зрения=> ',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
TestTrialQnA_Ans = keyboard.Keyboard()
TestTrialQnA_text2 = visual.TextStim(win=win, name='TestTrialQnA_text2',
    text='другое\n||\nv',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
polygon_centr = visual.ShapeStim(
    win=win, name='polygon_centr', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "InstBegin"
InstBeginClock = core.Clock()
InstBegin_text = visual.TextStim(win=win, name='InstBegin_text',
    text='Сейчас начнется основная часть эксперимента.\nБудьте внимательны, не отвлекайтесь.\n\nЧтобы начать, нажмите ПРОБЕЛ.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
InstBegin_keyresp = keyboard.Keyboard()

# Initialize components for Routine "TrialSD"
TrialSDClock = core.Clock()
TrialSD_keyresp = keyboard.Keyboard()
TrialSD_stimulus = visual.ImageStim(
    win=win,
    name='TrialSD_stimulus', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.27), size=(0.08, 0.03),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
TrialSD_image = visual.ImageStim(
    win=win,
    name='TrialSD_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.7, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
TrialSD_text = visual.TextStim(win=win, name='TrialSD_text',
    text="нажмите '<=' для ДРУГОЕ         нажмите '=>' для ТО ЖЕ",
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
polygon_centr = visual.ShapeStim(
    win=win, name='polygon_centr', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "TrialQnA"
TrialQnAClock = core.Clock()
TrialQnA_text = visual.TextStim(win=win, name='TrialQnA_text',
    text='Как ты решал?',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
TrialQnA_Ans = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
polygon_centr = visual.ShapeStim(
    win=win, name='polygon_centr', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
text_Ending = visual.TextStim(win=win, name='text_Ending',
    text='Спасибо за участие в эксперименте!\nОбратитесь к экспериментатору для дальнейших инструкций.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Ending = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Hello"-------
continueRoutine = True
# update component parameters for each repeat
helloKey.keys = []
helloKey.rt = []
_helloKey_allKeys = []
# keep track of which components have finished
HelloComponents = [helloText, helloKey]
for thisComponent in HelloComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
HelloClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Hello"-------
while continueRoutine:
    # get current time
    t = HelloClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=HelloClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *helloText* updates
    if helloText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloText.frameNStart = frameN  # exact frame index
        helloText.tStart = t  # local t and not account for scr refresh
        helloText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloText, 'tStartRefresh')  # time at next scr refresh
        helloText.setAutoDraw(True)
    
    # *helloKey* updates
    waitOnFlip = False
    if helloKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloKey.frameNStart = frameN  # exact frame index
        helloKey.tStart = t  # local t and not account for scr refresh
        helloKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloKey, 'tStartRefresh')  # time at next scr refresh
        helloKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(helloKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(helloKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if helloKey.status == STARTED and not waitOnFlip:
        theseKeys = helloKey.getKeys(keyList=['space'], waitRelease=False)
        _helloKey_allKeys.extend(theseKeys)
        if len(_helloKey_allKeys):
            helloKey.keys = _helloKey_allKeys[-1].name  # just the last key pressed
            helloKey.rt = _helloKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in HelloComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Hello"-------
for thisComponent in HelloComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Hello" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructionMR"-------
continueRoutine = True
# update component parameters for each repeat
InstMR_keyresp.keys = []
InstMR_keyresp.rt = []
_InstMR_keyresp_allKeys = []
# keep track of which components have finished
InstructionMRComponents = [InstMR_text, InstMR_keyresp, InstMR_image, InstMR_stimulus]
for thisComponent in InstructionMRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionMRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionMR"-------
while continueRoutine:
    # get current time
    t = InstructionMRClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionMRClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstMR_text* updates
    if InstMR_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstMR_text.frameNStart = frameN  # exact frame index
        InstMR_text.tStart = t  # local t and not account for scr refresh
        InstMR_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstMR_text, 'tStartRefresh')  # time at next scr refresh
        InstMR_text.setAutoDraw(True)
    
    # *InstMR_keyresp* updates
    waitOnFlip = False
    if InstMR_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstMR_keyresp.frameNStart = frameN  # exact frame index
        InstMR_keyresp.tStart = t  # local t and not account for scr refresh
        InstMR_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstMR_keyresp, 'tStartRefresh')  # time at next scr refresh
        InstMR_keyresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstMR_keyresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstMR_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstMR_keyresp.status == STARTED and not waitOnFlip:
        theseKeys = InstMR_keyresp.getKeys(keyList=['space'], waitRelease=False)
        _InstMR_keyresp_allKeys.extend(theseKeys)
        if len(_InstMR_keyresp_allKeys):
            InstMR_keyresp.keys = _InstMR_keyresp_allKeys[-1].name  # just the last key pressed
            InstMR_keyresp.rt = _InstMR_keyresp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *InstMR_image* updates
    if InstMR_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstMR_image.frameNStart = frameN  # exact frame index
        InstMR_image.tStart = t  # local t and not account for scr refresh
        InstMR_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstMR_image, 'tStartRefresh')  # time at next scr refresh
        InstMR_image.setAutoDraw(True)
    
    # *InstMR_stimulus* updates
    if InstMR_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstMR_stimulus.frameNStart = frameN  # exact frame index
        InstMR_stimulus.tStart = t  # local t and not account for scr refresh
        InstMR_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstMR_stimulus, 'tStartRefresh')  # time at next scr refresh
        InstMR_stimulus.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionMRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionMR"-------
for thisComponent in InstructionMRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if InstMR_keyresp.keys in ['', [], None]:  # No response was made
    InstMR_keyresp.keys = None
thisExp.addData('InstMR_keyresp.keys',InstMR_keyresp.keys)
if InstMR_keyresp.keys != None:  # we had a response
    thisExp.addData('InstMR_keyresp.rt', InstMR_keyresp.rt)
thisExp.nextEntry()
# the Routine "InstructionMR" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructionQnA"-------
continueRoutine = True
# update component parameters for each repeat
InstQnA_keyresp.keys = []
InstQnA_keyresp.rt = []
_InstQnA_keyresp_allKeys = []
# keep track of which components have finished
InstructionQnAComponents = [InstQnA_text, InstQnA_keyresp]
for thisComponent in InstructionQnAComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionQnAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionQnA"-------
while continueRoutine:
    # get current time
    t = InstructionQnAClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionQnAClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstQnA_text* updates
    if InstQnA_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstQnA_text.frameNStart = frameN  # exact frame index
        InstQnA_text.tStart = t  # local t and not account for scr refresh
        InstQnA_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstQnA_text, 'tStartRefresh')  # time at next scr refresh
        InstQnA_text.setAutoDraw(True)
    
    # *InstQnA_keyresp* updates
    waitOnFlip = False
    if InstQnA_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstQnA_keyresp.frameNStart = frameN  # exact frame index
        InstQnA_keyresp.tStart = t  # local t and not account for scr refresh
        InstQnA_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstQnA_keyresp, 'tStartRefresh')  # time at next scr refresh
        InstQnA_keyresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstQnA_keyresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstQnA_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstQnA_keyresp.status == STARTED and not waitOnFlip:
        theseKeys = InstQnA_keyresp.getKeys(keyList=['space'], waitRelease=False)
        _InstQnA_keyresp_allKeys.extend(theseKeys)
        if len(_InstQnA_keyresp_allKeys):
            InstQnA_keyresp.keys = _InstQnA_keyresp_allKeys[-1].name  # just the last key pressed
            InstQnA_keyresp.rt = _InstQnA_keyresp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionQnAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionQnA"-------
for thisComponent in InstructionQnAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if InstQnA_keyresp.keys in ['', [], None]:  # No response was made
    InstQnA_keyresp.keys = None
thisExp.addData('InstQnA_keyresp.keys',InstQnA_keyresp.keys)
if InstQnA_keyresp.keys != None:  # we had a response
    thisExp.addData('InstQnA_keyresp.rt', InstQnA_keyresp.rt)
thisExp.nextEntry()
# the Routine "InstructionQnA" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstTest"-------
continueRoutine = True
# update component parameters for each repeat
InstTest_keyresp.keys = []
InstTest_keyresp.rt = []
_InstTest_keyresp_allKeys = []
# keep track of which components have finished
InstTestComponents = [InstTest_text, InstTest_keyresp]
for thisComponent in InstTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstTest"-------
while continueRoutine:
    # get current time
    t = InstTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstTest_text* updates
    if InstTest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstTest_text.frameNStart = frameN  # exact frame index
        InstTest_text.tStart = t  # local t and not account for scr refresh
        InstTest_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstTest_text, 'tStartRefresh')  # time at next scr refresh
        InstTest_text.setAutoDraw(True)
    
    # *InstTest_keyresp* updates
    waitOnFlip = False
    if InstTest_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstTest_keyresp.frameNStart = frameN  # exact frame index
        InstTest_keyresp.tStart = t  # local t and not account for scr refresh
        InstTest_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstTest_keyresp, 'tStartRefresh')  # time at next scr refresh
        InstTest_keyresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstTest_keyresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstTest_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstTest_keyresp.status == STARTED and not waitOnFlip:
        theseKeys = InstTest_keyresp.getKeys(keyList=['space'], waitRelease=False)
        _InstTest_keyresp_allKeys.extend(theseKeys)
        if len(_InstTest_keyresp_allKeys):
            InstTest_keyresp.keys = _InstTest_keyresp_allKeys[-1].name  # just the last key pressed
            InstTest_keyresp.rt = _InstTest_keyresp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstTest"-------
for thisComponent in InstTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if InstTest_keyresp.keys in ['', [], None]:  # No response was made
    InstTest_keyresp.keys = None
thisExp.addData('InstTest_keyresp.keys',InstTest_keyresp.keys)
if InstTest_keyresp.keys != None:  # we had a response
    thisExp.addData('InstTest_keyresp.rt', InstTest_keyresp.rt)
thisExp.nextEntry()
# the Routine "InstTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
testTrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file_2.xlsx', selection='12:16'),
    seed=None, name='testTrials')
thisExp.addLoop(testTrials)  # add the loop to the experiment
thisTestTrial = testTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
if thisTestTrial != None:
    for paramName in thisTestTrial:
        exec('{} = thisTestTrial[paramName]'.format(paramName))

for thisTestTrial in testTrials:
    currentLoop = testTrials
    # abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
    if thisTestTrial != None:
        for paramName in thisTestTrial:
            exec('{} = thisTestTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TestTrialMR"-------
    continueRoutine = True
    # update component parameters for each repeat
    TestTrialMR_keyresp.keys = []
    TestTrialMR_keyresp.rt = []
    _TestTrialMR_keyresp_allKeys = []
    TestTrialMR_stimulus.setImage(stimulifile)
    TestTrialMR_image.setImage(imagefile)
    # keep track of which components have finished
    TestTrialMRComponents = [TestTrialMR_keyresp, TestTrialMR_stimulus, TestTrialMR_image, TestTrialMR_text]
    for thisComponent in TestTrialMRComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestTrialMRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TestTrialMR"-------
    while continueRoutine:
        # get current time
        t = TestTrialMRClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestTrialMRClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TestTrialMR_keyresp* updates
        waitOnFlip = False
        if TestTrialMR_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TestTrialMR_keyresp.frameNStart = frameN  # exact frame index
            TestTrialMR_keyresp.tStart = t  # local t and not account for scr refresh
            TestTrialMR_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TestTrialMR_keyresp, 'tStartRefresh')  # time at next scr refresh
            TestTrialMR_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TestTrialMR_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TestTrialMR_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TestTrialMR_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = TestTrialMR_keyresp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _TestTrialMR_keyresp_allKeys.extend(theseKeys)
            if len(_TestTrialMR_keyresp_allKeys):
                TestTrialMR_keyresp.keys = _TestTrialMR_keyresp_allKeys[-1].name  # just the last key pressed
                TestTrialMR_keyresp.rt = _TestTrialMR_keyresp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *TestTrialMR_stimulus* updates
        if TestTrialMR_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TestTrialMR_stimulus.frameNStart = frameN  # exact frame index
            TestTrialMR_stimulus.tStart = t  # local t and not account for scr refresh
            TestTrialMR_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TestTrialMR_stimulus, 'tStartRefresh')  # time at next scr refresh
            TestTrialMR_stimulus.setAutoDraw(True)
        
        # *TestTrialMR_image* updates
        if TestTrialMR_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TestTrialMR_image.frameNStart = frameN  # exact frame index
            TestTrialMR_image.tStart = t  # local t and not account for scr refresh
            TestTrialMR_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TestTrialMR_image, 'tStartRefresh')  # time at next scr refresh
            TestTrialMR_image.setAutoDraw(True)
        
        # *TestTrialMR_text* updates
        if TestTrialMR_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TestTrialMR_text.frameNStart = frameN  # exact frame index
            TestTrialMR_text.tStart = t  # local t and not account for scr refresh
            TestTrialMR_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TestTrialMR_text, 'tStartRefresh')  # time at next scr refresh
            TestTrialMR_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestTrialMRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestTrialMR"-------
    for thisComponent in TestTrialMRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TestTrialMR_keyresp.keys in ['', [], None]:  # No response was made
        TestTrialMR_keyresp.keys = None
    testTrials.addData('TestTrialMR_keyresp.keys',TestTrialMR_keyresp.keys)
    if TestTrialMR_keyresp.keys != None:  # we had a response
        testTrials.addData('TestTrialMR_keyresp.rt', TestTrialMR_keyresp.rt)
    # the Routine "TestTrialMR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [polygon_centr]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_centr* updates
        if polygon_centr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_centr.frameNStart = frameN  # exact frame index
            polygon_centr.tStart = t  # local t and not account for scr refresh
            polygon_centr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_centr, 'tStartRefresh')  # time at next scr refresh
            polygon_centr.setAutoDraw(True)
        if polygon_centr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_centr.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_centr.tStop = t  # not accounting for scr refresh
                polygon_centr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_centr, 'tStopRefresh')  # time at next scr refresh
                polygon_centr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "TestTrialQnA"-------
    continueRoutine = True
    # update component parameters for each repeat
    TestTrialQnA_Ans.keys = []
    TestTrialQnA_Ans.rt = []
    _TestTrialQnA_Ans_allKeys = []
    # keep track of which components have finished
    TestTrialQnAComponents = [TestTrialQnA_text, TestTrialQnA_Ans, TestTrialQnA_text2]
    for thisComponent in TestTrialQnAComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestTrialQnAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TestTrialQnA"-------
    while continueRoutine:
        # get current time
        t = TestTrialQnAClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestTrialQnAClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TestTrialQnA_text* updates
        if TestTrialQnA_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TestTrialQnA_text.frameNStart = frameN  # exact frame index
            TestTrialQnA_text.tStart = t  # local t and not account for scr refresh
            TestTrialQnA_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TestTrialQnA_text, 'tStartRefresh')  # time at next scr refresh
            TestTrialQnA_text.setAutoDraw(True)
        
        # *TestTrialQnA_Ans* updates
        waitOnFlip = False
        if TestTrialQnA_Ans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TestTrialQnA_Ans.frameNStart = frameN  # exact frame index
            TestTrialQnA_Ans.tStart = t  # local t and not account for scr refresh
            TestTrialQnA_Ans.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TestTrialQnA_Ans, 'tStartRefresh')  # time at next scr refresh
            TestTrialQnA_Ans.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TestTrialQnA_Ans.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TestTrialQnA_Ans.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TestTrialQnA_Ans.status == STARTED and not waitOnFlip:
            theseKeys = TestTrialQnA_Ans.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _TestTrialQnA_Ans_allKeys.extend(theseKeys)
            if len(_TestTrialQnA_Ans_allKeys):
                TestTrialQnA_Ans.keys = _TestTrialQnA_Ans_allKeys[-1].name  # just the last key pressed
                TestTrialQnA_Ans.rt = _TestTrialQnA_Ans_allKeys[-1].rt
                # was this correct?
                if (TestTrialQnA_Ans.keys == str('')) or (TestTrialQnA_Ans.keys == ''):
                    TestTrialQnA_Ans.corr = 1
                else:
                    TestTrialQnA_Ans.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *TestTrialQnA_text2* updates
        if TestTrialQnA_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TestTrialQnA_text2.frameNStart = frameN  # exact frame index
            TestTrialQnA_text2.tStart = t  # local t and not account for scr refresh
            TestTrialQnA_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TestTrialQnA_text2, 'tStartRefresh')  # time at next scr refresh
            TestTrialQnA_text2.setAutoDraw(True)
        if TestTrialQnA_text2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TestTrialQnA_text2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                TestTrialQnA_text2.tStop = t  # not accounting for scr refresh
                TestTrialQnA_text2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TestTrialQnA_text2, 'tStopRefresh')  # time at next scr refresh
                TestTrialQnA_text2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestTrialQnAComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestTrialQnA"-------
    for thisComponent in TestTrialQnAComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TestTrialQnA_Ans.keys in ['', [], None]:  # No response was made
        TestTrialQnA_Ans.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           TestTrialQnA_Ans.corr = 1;  # correct non-response
        else:
           TestTrialQnA_Ans.corr = 0;  # failed to respond (incorrectly)
    # store data for testTrials (TrialHandler)
    testTrials.addData('TestTrialQnA_Ans.keys',TestTrialQnA_Ans.keys)
    testTrials.addData('TestTrialQnA_Ans.corr', TestTrialQnA_Ans.corr)
    if TestTrialQnA_Ans.keys != None:  # we had a response
        testTrials.addData('TestTrialQnA_Ans.rt', TestTrialQnA_Ans.rt)
    testTrials.addData('TestTrialQnA_text2.started', TestTrialQnA_text2.tStartRefresh)
    testTrials.addData('TestTrialQnA_text2.stopped', TestTrialQnA_text2.tStopRefresh)
    # the Routine "TestTrialQnA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [polygon_centr]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_centr* updates
        if polygon_centr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_centr.frameNStart = frameN  # exact frame index
            polygon_centr.tStart = t  # local t and not account for scr refresh
            polygon_centr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_centr, 'tStartRefresh')  # time at next scr refresh
            polygon_centr.setAutoDraw(True)
        if polygon_centr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_centr.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_centr.tStop = t  # not accounting for scr refresh
                polygon_centr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_centr, 'tStopRefresh')  # time at next scr refresh
                polygon_centr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'testTrials'


# ------Prepare to start Routine "InstBegin"-------
continueRoutine = True
# update component parameters for each repeat
InstBegin_keyresp.keys = []
InstBegin_keyresp.rt = []
_InstBegin_keyresp_allKeys = []
# keep track of which components have finished
InstBeginComponents = [InstBegin_text, InstBegin_keyresp]
for thisComponent in InstBeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstBeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstBegin"-------
while continueRoutine:
    # get current time
    t = InstBeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstBeginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstBegin_text* updates
    if InstBegin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstBegin_text.frameNStart = frameN  # exact frame index
        InstBegin_text.tStart = t  # local t and not account for scr refresh
        InstBegin_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstBegin_text, 'tStartRefresh')  # time at next scr refresh
        InstBegin_text.setAutoDraw(True)
    
    # *InstBegin_keyresp* updates
    waitOnFlip = False
    if InstBegin_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstBegin_keyresp.frameNStart = frameN  # exact frame index
        InstBegin_keyresp.tStart = t  # local t and not account for scr refresh
        InstBegin_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstBegin_keyresp, 'tStartRefresh')  # time at next scr refresh
        InstBegin_keyresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstBegin_keyresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstBegin_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstBegin_keyresp.status == STARTED and not waitOnFlip:
        theseKeys = InstBegin_keyresp.getKeys(keyList=['space'], waitRelease=False)
        _InstBegin_keyresp_allKeys.extend(theseKeys)
        if len(_InstBegin_keyresp_allKeys):
            InstBegin_keyresp.keys = _InstBegin_keyresp_allKeys[-1].name  # just the last key pressed
            InstBegin_keyresp.rt = _InstBegin_keyresp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstBeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstBegin"-------
for thisComponent in InstBeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if InstBegin_keyresp.keys in ['', [], None]:  # No response was made
    InstBegin_keyresp.keys = None
thisExp.addData('InstBegin_keyresp.keys',InstBegin_keyresp.keys)
if InstBegin_keyresp.keys != None:  # we had a response
    thisExp.addData('InstBegin_keyresp.rt', InstBegin_keyresp.rt)
thisExp.nextEntry()
# the Routine "InstBegin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loopSD = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file_2.xlsx'),
    seed=None, name='loopSD')
thisExp.addLoop(loopSD)  # add the loop to the experiment
thisLoopSD = loopSD.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopSD.rgb)
if thisLoopSD != None:
    for paramName in thisLoopSD:
        exec('{} = thisLoopSD[paramName]'.format(paramName))

for thisLoopSD in loopSD:
    currentLoop = loopSD
    # abbreviate parameter names if possible (e.g. rgb = thisLoopSD.rgb)
    if thisLoopSD != None:
        for paramName in thisLoopSD:
            exec('{} = thisLoopSD[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TrialSD"-------
    continueRoutine = True
    # update component parameters for each repeat
    TrialSD_keyresp.keys = []
    TrialSD_keyresp.rt = []
    _TrialSD_keyresp_allKeys = []
    TrialSD_stimulus.setImage(stimulifile)
    TrialSD_image.setImage(imagefile)
    # keep track of which components have finished
    TrialSDComponents = [TrialSD_keyresp, TrialSD_stimulus, TrialSD_image, TrialSD_text]
    for thisComponent in TrialSDComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialSDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TrialSD"-------
    while continueRoutine:
        # get current time
        t = TrialSDClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialSDClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TrialSD_keyresp* updates
        waitOnFlip = False
        if TrialSD_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialSD_keyresp.frameNStart = frameN  # exact frame index
            TrialSD_keyresp.tStart = t  # local t and not account for scr refresh
            TrialSD_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialSD_keyresp, 'tStartRefresh')  # time at next scr refresh
            TrialSD_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TrialSD_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TrialSD_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TrialSD_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = TrialSD_keyresp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _TrialSD_keyresp_allKeys.extend(theseKeys)
            if len(_TrialSD_keyresp_allKeys):
                TrialSD_keyresp.keys = _TrialSD_keyresp_allKeys[-1].name  # just the last key pressed
                TrialSD_keyresp.rt = _TrialSD_keyresp_allKeys[-1].rt
                # was this correct?
                if (TrialSD_keyresp.keys == str(corrAns)) or (TrialSD_keyresp.keys == corrAns):
                    TrialSD_keyresp.corr = 1
                else:
                    TrialSD_keyresp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *TrialSD_stimulus* updates
        if TrialSD_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialSD_stimulus.frameNStart = frameN  # exact frame index
            TrialSD_stimulus.tStart = t  # local t and not account for scr refresh
            TrialSD_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialSD_stimulus, 'tStartRefresh')  # time at next scr refresh
            TrialSD_stimulus.setAutoDraw(True)
        
        # *TrialSD_image* updates
        if TrialSD_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialSD_image.frameNStart = frameN  # exact frame index
            TrialSD_image.tStart = t  # local t and not account for scr refresh
            TrialSD_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialSD_image, 'tStartRefresh')  # time at next scr refresh
            TrialSD_image.setAutoDraw(True)
        
        # *TrialSD_text* updates
        if TrialSD_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialSD_text.frameNStart = frameN  # exact frame index
            TrialSD_text.tStart = t  # local t and not account for scr refresh
            TrialSD_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialSD_text, 'tStartRefresh')  # time at next scr refresh
            TrialSD_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialSDComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TrialSD"-------
    for thisComponent in TrialSDComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TrialSD_keyresp.keys in ['', [], None]:  # No response was made
        TrialSD_keyresp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           TrialSD_keyresp.corr = 1;  # correct non-response
        else:
           TrialSD_keyresp.corr = 0;  # failed to respond (incorrectly)
    # store data for loopSD (TrialHandler)
    loopSD.addData('TrialSD_keyresp.keys',TrialSD_keyresp.keys)
    loopSD.addData('TrialSD_keyresp.corr', TrialSD_keyresp.corr)
    if TrialSD_keyresp.keys != None:  # we had a response
        loopSD.addData('TrialSD_keyresp.rt', TrialSD_keyresp.rt)
    loopSD.addData('TrialSD_keyresp.started', TrialSD_keyresp.tStartRefresh)
    loopSD.addData('TrialSD_keyresp.stopped', TrialSD_keyresp.tStopRefresh)
    # the Routine "TrialSD" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [polygon_centr]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_centr* updates
        if polygon_centr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_centr.frameNStart = frameN  # exact frame index
            polygon_centr.tStart = t  # local t and not account for scr refresh
            polygon_centr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_centr, 'tStartRefresh')  # time at next scr refresh
            polygon_centr.setAutoDraw(True)
        if polygon_centr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_centr.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_centr.tStop = t  # not accounting for scr refresh
                polygon_centr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_centr, 'tStopRefresh')  # time at next scr refresh
                polygon_centr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "TrialQnA"-------
    continueRoutine = True
    # update component parameters for each repeat
    TrialQnA_Ans.keys = []
    TrialQnA_Ans.rt = []
    _TrialQnA_Ans_allKeys = []
    # keep track of which components have finished
    TrialQnAComponents = [TrialQnA_text, TrialQnA_Ans]
    for thisComponent in TrialQnAComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialQnAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TrialQnA"-------
    while continueRoutine:
        # get current time
        t = TrialQnAClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialQnAClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TrialQnA_text* updates
        if TrialQnA_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialQnA_text.frameNStart = frameN  # exact frame index
            TrialQnA_text.tStart = t  # local t and not account for scr refresh
            TrialQnA_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialQnA_text, 'tStartRefresh')  # time at next scr refresh
            TrialQnA_text.setAutoDraw(True)
        
        # *TrialQnA_Ans* updates
        waitOnFlip = False
        if TrialQnA_Ans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialQnA_Ans.frameNStart = frameN  # exact frame index
            TrialQnA_Ans.tStart = t  # local t and not account for scr refresh
            TrialQnA_Ans.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialQnA_Ans, 'tStartRefresh')  # time at next scr refresh
            TrialQnA_Ans.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TrialQnA_Ans.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TrialQnA_Ans.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TrialQnA_Ans.status == STARTED and not waitOnFlip:
            theseKeys = TrialQnA_Ans.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _TrialQnA_Ans_allKeys.extend(theseKeys)
            if len(_TrialQnA_Ans_allKeys):
                TrialQnA_Ans.keys = _TrialQnA_Ans_allKeys[-1].name  # just the last key pressed
                TrialQnA_Ans.rt = _TrialQnA_Ans_allKeys[-1].rt
                # was this correct?
                if (TrialQnA_Ans.keys == str('')) or (TrialQnA_Ans.keys == ''):
                    TrialQnA_Ans.corr = 1
                else:
                    TrialQnA_Ans.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialQnAComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TrialQnA"-------
    for thisComponent in TrialQnAComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TrialQnA_Ans.keys in ['', [], None]:  # No response was made
        TrialQnA_Ans.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           TrialQnA_Ans.corr = 1;  # correct non-response
        else:
           TrialQnA_Ans.corr = 0;  # failed to respond (incorrectly)
    # store data for loopSD (TrialHandler)
    loopSD.addData('TrialQnA_Ans.keys',TrialQnA_Ans.keys)
    loopSD.addData('TrialQnA_Ans.corr', TrialQnA_Ans.corr)
    if TrialQnA_Ans.keys != None:  # we had a response
        loopSD.addData('TrialQnA_Ans.rt', TrialQnA_Ans.rt)
    # the Routine "TrialQnA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [polygon_centr]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_centr* updates
        if polygon_centr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_centr.frameNStart = frameN  # exact frame index
            polygon_centr.tStart = t  # local t and not account for scr refresh
            polygon_centr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_centr, 'tStartRefresh')  # time at next scr refresh
            polygon_centr.setAutoDraw(True)
        if polygon_centr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_centr.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_centr.tStop = t  # not accounting for scr refresh
                polygon_centr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_centr, 'tStopRefresh')  # time at next scr refresh
                polygon_centr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loopSD'


# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_Ending.keys = []
key_resp_Ending.rt = []
_key_resp_Ending_allKeys = []
# keep track of which components have finished
GoodbyeComponents = [text_Ending, key_resp_Ending]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Ending* updates
    if text_Ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Ending.frameNStart = frameN  # exact frame index
        text_Ending.tStart = t  # local t and not account for scr refresh
        text_Ending.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Ending, 'tStartRefresh')  # time at next scr refresh
        text_Ending.setAutoDraw(True)
    
    # *key_resp_Ending* updates
    waitOnFlip = False
    if key_resp_Ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Ending.frameNStart = frameN  # exact frame index
        key_resp_Ending.tStart = t  # local t and not account for scr refresh
        key_resp_Ending.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Ending, 'tStartRefresh')  # time at next scr refresh
        key_resp_Ending.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Ending.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Ending.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Ending.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Ending.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_Ending_allKeys.extend(theseKeys)
        if len(_key_resp_Ending_allKeys):
            key_resp_Ending.keys = _key_resp_Ending_allKeys[-1].name  # just the last key pressed
            key_resp_Ending.rt = _key_resp_Ending_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_Ending.keys in ['', [], None]:  # No response was made
    key_resp_Ending.keys = None
thisExp.addData('key_resp_Ending.keys',key_resp_Ending.keys)
if key_resp_Ending.keys != None:  # we had a response
    thisExp.addData('key_resp_Ending.rt', key_resp_Ending.rt)
thisExp.nextEntry()
# the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
