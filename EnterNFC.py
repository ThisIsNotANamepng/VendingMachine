import PySimpleGUI as sg
import requests
import hashlib
import json
import time
import os


sg.theme('DarkGrey13')	

layout = [
	[sg.Text('Please scan your tag', size =(30, 30))],
	[sg.Text('NFC', size =(15, 1)), sg.InputText(password_char = '*')],
	[sg.Submit(), sg.Cancel()]
]

window = sg.Window('Enter your NFC tag', layout).Finalize()
#window.Maximize()

event, values = window.read()


input = values[0]

try:

    y = json.loads(input)

except:
    print("Failureexcet")
    sg.popup_auto_close('Credentials incorrect.Try using your actual tag.')
    #os.system('python3 MainScreen.py')
else:
    password = (y["p"]) 
    username = (y["u"]) 
    print(password)
    print(username)

    x = requests.get("https://JoshCoinServer.codeeatspennies.repl.co/a", auth = (username, password))


    json = json.loads(x.text)
    success = (json["success"])
    #{"u":"Jack", "p":"password"}

    if success == True:
        print("Good job")
        #playsound('audio.mp3')
        os.system('python3 showimage.py')
        #Release snack
    else:
        print("Failure")
window.close()
