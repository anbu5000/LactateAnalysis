#WIP Do Not Use

import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkTeal9')

df = pd.read_excel('LactateLogTest.xlsx')

layout = [
    [sg.Text('Fill out the following fields:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.CalendarButton('Date', size=(10,1), key='Date'), sg.Text('Date', size=(15,1))],
    [sg.Text('Workout rep length:', size=(15,1)),
        sg.Checkbox('6min', key=6),
        sg.Checkbox('3min', key=3),
        sg.Checkbox('1min', key=1)],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        df = df.concat(values, ignore_index=True)
        df.to_excel('LactateLogTest.xlsx', index=False)
        sg.popup('Data saved!')
        print(event, values)