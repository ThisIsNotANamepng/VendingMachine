import PySimpleGUI as sg
import time
import threading

sg.theme('DarkGrey13')


def close():
    time.sleep(3)
    window.close()


    
    

layout = [[sg.Image('IMG_20220507_174233~3.png', size=(300,300))], [sg.popup_timed('jorsh', auto_close=True, auto_close_duration=3, image='IMG_20220507_174233~3.png')]]

# Create the window
window = sg.Window('Wow! A Josh!', layout).Finalize()
window.Maximize()


while True:
    event, values = window.read()
    print("stuff")




    if event == event == sg.WIN_CLOSED:
        break


window.close()







