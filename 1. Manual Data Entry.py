# Step 1: Manually enter basic metadata for images

import PySimpleGUI as sg
import pandas as pd
import openpyxl

# Add some color to the window
Theme = 'Topanga'
sg.theme(Theme)

EXCEL_FILE = 'Data_Entry.xlsx'
df = pd.read_excel('Data_Entry.xlsx', sheet_name="Data Entry")

layout = [
    [sg.Text('Press Exit once finished entering data for all images to save progress')],
    [sg.Text('To enter more data, manually clear fields as necessary after submission of each entry.')],
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('__________________________________')],
    [sg.Text('Current File Name is case sensitive and must match exactly')],
    [sg.Text('Current File Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('Image Subject', size=(15,1)), sg.InputText(key='Subject')],
    [sg.Text('Input coordinates in decimal degrees:')],
    [sg.Text('Latitude', size=(15,1)), sg.InputText(key='Latitude')],
    [sg.Text('Longitude', size=(15,1)), sg.InputText(key='Longitude')],
    [sg.Text('Manual Tag Input', size=(15,1)), sg.InputText(key='Manual Tag Input')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
window.close()
