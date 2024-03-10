# Window to be used with Number Guessing Game
#
# Created by: MonkikoBytes
# Created on: 09-06-2021
# Last Revised on: 03-10-2024
# Version: 2.1.0
#
import PySimpleGUI as sg
from random import randrange
#
#
sg.theme('DarkAmber')
#
#
def Randomize():
    num = randrange(101)
    return num
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
    num = Randomize()
    layout = [[sg.Text('Guess a number between 1-100:', key='-WORDS-'), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Input(key='-IN-')],
            [sg.Button('Submit'), sg.Button('Exit')]]

    window = sg.Window("Guess That Number!", layout)

    while True:
        event, values = window.read()
        print(event, values)
        response = values['-IN-']
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Submit' and values['-IN-']:
            response = int(response)
            try:
                if response == num:
                    window.close()
                    GuessCorrect()
                elif response < num:
                    window['-WORDS-'].update('OOPS! That was too low. Try again.')
                    window['-OUTPUT-'].update(values['-IN-'])
                elif response > num:
                    window['-WORDS-'].update('OOPS! That was too high. Try again.')
                    window['-OUTPUT-'].update(values['-IN-'])
            except:
                window['-OUTPUT-'].update('Invalid Response. Try guessing a number between 1-100')
    window.close()

#
#
def GuessCorrect():
    layout = [[sg.Text('You guessed correctly. Good job!')],
                [sg.Button('Play Again'), sg.Button('Exit')]]
    
    window = sg.Window('Guess That Number!', layout)

    event, values = window.read()
    if event == 'Play Again':
        window.close()
        Randomize()
        Announcement()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()

#
#
Randomize()
Announcement()