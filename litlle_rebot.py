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
#import nltk
from nltk.tokenize import word_tokenize
#nltk.download('punkt')

#
#r = sr.Recognizer()
#with sr.Microphone() as source:
#    print("Say something!")
#    r.adjust_for_ambient_noise(source)
#    audio = r.listen(source)
#    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))

def commandProcessing(command, commandType):
    "here we wil use nltk for tokenizing audio and get the details of command"
    if commandType == "welcome":
        response("hello, Mr. brahim i m your robot what i can do for you ?")
    elif commandType == "move": 
        words = word_tokenize(command)
        number = [s for s in words if s.isnumeric()]
        responseString = "Ok, I move " + number[0] + " cm forward"
        response(responseString)
        print("A:", number[0])
    elif commandType == "back": 
        words = word_tokenize(command)
        number = [s for s in words if s.isnumeric()]
        responseString = "Ok, I move " + number[0] + " cm to the back"
        response(responseString)
        print("R:", number[0])
    elif commandType == "rotate": 
        words = word_tokenize(command)
        number = [s for s in words if s.isnumeric()]
        responseString = "Ok, I rotate " + number[0] + " degrees"
        response(responseString)
        print("Ro:", number[0])
    elif commandType == "shutdown": 
        response("Bye bye Mr. brahim. have a nice day")
        sys.exit()
    else:
        pass



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
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
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
    if "little robot" in command:
        commandProcessing(command, "welcome")
    elif "move" in command:
        commandProcessing(command, "move")
    elif "back" in command:
        commandProcessing(command, "back")
    elif "rotate" in command:
        commandProcessing(command, "rotate")
    elif "shut down" in command: 
        commandProcessing(command, "shutdoawn")

while True: 
    littleRebot(myCommand())
