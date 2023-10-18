import PySimpleGUI as sg
import backend as bk

sg.theme('DarkAmber')

layout = [
          [sg.Text('Sign Up')],
          [sg.Text('Name'), sg.InputText()],
          [sg.Text('Email'), sg.InputText()],
          [sg.Text('Username'), sg.InputText()],
          [sg.Text('Password'), sg.InputText()],
          [sg.Button('Submit', key='submit')],
          ]

window = sg.Window('Sign Up', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'submit':
        print("Submit button pressed")