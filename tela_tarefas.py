from doctest import BLANKLINE_MARKER
import PySimpleGUI as sg

def tela_tarefas():
    sg.theme('BlueMono')

    layout = [[sg.Text('Disco Status')]]

    window = sg.Window('Tarefas',layout)

    while True:
        event, Values = window.read()
        if event == sg.WIN_CLOSED:
           break
    window.close()

