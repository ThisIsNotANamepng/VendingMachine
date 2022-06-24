import PySimpleGUI as sg
import time
import threading
from playsound import playsound


sg.theme('DarkGrey13')


def close():
    time.sleep(3)
    window.close()



    

layout = [[sg.Image('HappyJosh.png', size=(800,480))], [sg.popup_timed('jorsh', auto_close=True, auto_close_duration=3, image='HappyJosh.png')]]

# Create the window
window = sg.Window('Wow!', layout).Finalize()
window.Maximize()


while True:
    event, values = window.read()
    print("stuff")




    if event == event == sg.WIN_CLOSED:
        break

print(12313)
window.close()







