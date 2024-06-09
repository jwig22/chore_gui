import PySimpleGUI as sg

chores = ['Morning', 'Afternoon', 'Zone', 'Evening']

# All the stuff inside your window.
layout = [  [sg.Checkbox(text=chores[0],key=chores[0])],
            [sg.Checkbox(text=chores[1],key=chores[1])],
            [sg.Checkbox(text=chores[2],key=chores[2])],
            [sg.Checkbox(text=chores[3],key=chores[3])],
            [sg.Button('Submit'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Kid 1 Chores', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'): # if user closes window or clicks cancel
        break
    print(f'Values: {values}')


window.close()
