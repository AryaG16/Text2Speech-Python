# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:11:30 2021

@author: Aryanand
"""

import pyttsx3

def talk(text,PATH):
    a.say(text)
    a.save_to_file(text, PATH)
    a.runAndWait()
    
text=input("Text To Speech: ")
filename=input("Filename: ")
PATH="D:\\PYTHON exps\\"+filename+".mp3"

a=pyttsx3.init()


talk(text,PATH)

