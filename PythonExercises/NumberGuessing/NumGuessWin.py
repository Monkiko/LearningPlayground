# Window to be used with Number Guessing Game
#
# Created by: Ian Rivera-Leandry
# Created on: 09-04-2021
# Last Revised on: 09-04-2021
#
import PySimpleGUI as sg
#
#
sg.theme('DarkAmber')
#
#
layout = [[sg.Text('Let\'s play a game! Guess a number between 1-100:'), sg.Text(size=(15,1), key='-OUTPUT-')], [sg.Input(key='-IN-')], [sg.Button('Submit'), sg.Button('Exit')]]

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