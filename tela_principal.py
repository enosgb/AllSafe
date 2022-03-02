from cgitb import text
from tkinter import Button, font
import PySimpleGUI as sg
from img_tags import *
from armazenamento import *



sg.theme('BlueMono')
layout = [[sg.Button('', image_data=shield, button_color=('light blue', sg.theme_background_color()),
                      border_width=0, ),sg.Button('', image_data=UNIFESO,button_color=('light blue',sg.theme_background_color()),border_width=0)]]
layout += [[sg.Text('Full Scan               ',font='Helvetica 16 bold italic',text_color='white'),sg.Button(' Iniciar Verificação', image_data=image_large_rectangle,font='Helvetica 12 bold italic', button_color=('light blue', sg.theme_background_color()),
                      border_width=0, )],
         [sg.Text('Verificar Arquivo  ',font='Helvetica 16 bold italic',text_color='white'),sg.Button('Selecionar Arquivo', image_data=image_large_rectangle, font='Helvetica 12 bold italic', button_color=('light blue', sg.theme_background_color()),
                      border_width=0, )],
         [sg.Button('Tarefas', image_data=image_large_rectangle, font='Helvetica 12 bold italic', button_color=('light blue', sg.theme_background_color()),
                      border_width=0, ),sg.Button('Configurações', image_data=image_large_rectangle, font='Helvetica 12 bold italic', button_color=('light blue', sg.theme_background_color()),
                      border_width=0, ),],
         
]

window = sg.Window('AllSafe Antivirus',layout)

while True:
    event, Values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()