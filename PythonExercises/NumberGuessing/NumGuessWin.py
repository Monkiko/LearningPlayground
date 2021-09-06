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
    global response
    layout = [[sg.Text('Guess a number between 1-100:'), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.InputText(key='-IN-')],
            [sg.Button('Submit'), sg.Button('Exit')]]

    window = sg.Window("Guess That Number!", layout)

    event, values = window.read()
    response = print(values['-IN-'])
    if event == 'Submit':
        window.close()
        InputCheck()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()


def InputCheck():
    global response
    global guess
    try:
        guess = int(response)
        NumGuess()
    except ValueError:
        InvInput()


def InvInput():
    global response
    layout = [[sg.Text('Invalid value. Please enter a number between 1-100'), sg.Text(size=(15,1))],
            [sg.InputText(key='-IN-')],
            [sg.Button('Submit'), sg.Button('Exit')]]

    window = sg.Window("Guess That Number!", layout)

    event, values = window.read()
    response = print(event, values['-IN-'])
    if event == 'Submit':
        window.close()
        InputCheck()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()



def NumGuess():
    global guess
    global num
    if guess == num:
        GuessCorrect()
    elif guess > num:
        GuessHigh()
    elif guess < num:
        GuessLow()


def GuessCorrect():
    global guess
    layout = [[sg.Text('You guessed correctly. Good job!'), sg.Text(size=(15,1))],
                [sg.Button('OK'), sg.Button('Exit')]]
    
    window = sg.Window('Guess That Number!', layout)

    event, values = window.read()
    if event == 'OK':
        window.close()
        End()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()


def GuessHigh():
    global guess
    layout = [[sg.Text('Guess a number between 1-100:'), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Input(key='-IN-')],
            [sg.Button('Submit'), sg.Button('Exit')]]

    window = sg.Window("Guess That Number!", layout)

    response = ['-IN-']

    event, values = window.read()
    if event == 'Submit':
        window.close()
        InputCheck()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()


def GuessLow():
    global guess
    layout = [[sg.Text('Guess a number between 1-100:'), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Input(key='-IN-')],
            [sg.Button('Submit'), sg.Button('Exit')]]

    window = sg.Window("Guess That Number!", layout)

    response = ['-IN-']

    event, values = window.read()
    if event == 'Submit':
        window.close()
        InputCheck()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
#
#
def End():
    layout = [[sg.Text('Would you like to play again?'), sg.Text(size=(15,1))],
                [sg.Button('OK'), sg.Button('Exit')]]
    
    window = sg.Window('Guess That Number!', layout)

    event, values = window.read()
    if event == 'OK':
        window.close()
        Randomize()
        Start()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()

Randomize()
Announcement()