# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:33:22 2019

@author: brahim.adref
"""

import speech_recognition as sr
import os
import sys
from gtts import gTTS
import pyttsx3 
#
#r = sr.Recognizer()
#with sr.Microphone() as source:
#    print("Say something!")
#    r.adjust_for_ambient_noise(source)
#    audio = r.listen(source)
#    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))

def response(audio):
    "speaks audio passed as argument"
    print(audio)
#    tts = gTTS(text=audio, lang='en')
#    tts.save("audio.mp3")
#    os.system("mpg321 audio.mp3")
#    for line in audio.splitlines():
#        os.system("say " + audio)
#        
    engine = pyttsx3.init()
    engine.setProperty('rate', 125) 
    
    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[1].id) 
    
    engine.say(audio)
    engine.runAndWait()
def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        #r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command

def littleRebot(command): 
    "if statements for executing commands"
    if "hello" in command:
        response("Hello, brahim i m your rebot what i can do for you")
    elif "fuck" in command:
        response("what are you saying si brahim shame on you")
    elif "shut down" in command: 
        response("Bye bye si brahim. have a nice day")
        sys.exit()

while True: 
    littleRebot(myCommand())
