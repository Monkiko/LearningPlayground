# Window to be used with Number Guessing Game
#
# Created by: Ian Rivera-Leandry
# Created on: 09-04-2021
# Last Revised on: 09-05-2021
#
import PySimpleGUI as sg
from random import randrange
#
#
sg.theme('DarkAmber')
#
#
def Randomize():
    global num
    num = randrange(101)
#
#

def Announcement():
    layout = [[sg.Text('Let\'s play a number guessing game!'), sg.Text(size=(15,1))],
                [sg.Button('OK'), sg.Button('Exit')]]
    
    window = sg.Window('Guess That Number!', layout)

    event, values = window.read()
    if event == 'OK':
        window.close()
        Start()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()

#
#
def Start():
    layout = [[sg.Text('Guess a number between 1-100:'), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Input(key='-IN-')],
            [sg.Button('Submit'), sg.Button('Exit')]]

    window = sg.Window("Guess That Number!", layout)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Submit':
            # Update the "output" text element to be the value of "input" element
            window['-OUTPUT-'].update(values['-IN-'])
    window.close()
#
#
Randomize()
Announcement()