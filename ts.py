import PySimpleGUI as sg
import sys


background = '#F0F0F0'
sg.SetOptions(window_location=(0, 0), margins=(0,0))
sg.theme('DarkGrey13')
layout = [[sg.Button("Row 1", size=(40, 24)), sg.Button("Row 2", size=(40, 24))], [sg.Button("Row 3", size=(40, 24)), sg.Button("Row 4", size=(40, 24))]]

# Create the window
window = sg.Window('JoshCoin', layout).Finalize()
window.Maximize()
# Create an event loop
while True:
    event, values = window.read()

    if event == event == sg.WIN_CLOSED:
        break
    elif event == "Row 1":
        print("1")
        import showimage
        sys.modules.pop('showimage')
    elif event == "Row 2":
        print("2")
    elif event == "Row 3":
        print("3")
    elif event == "Row 4":
        print("4")
window.close()