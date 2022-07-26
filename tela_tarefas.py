from cgitb import text
from doctest import BLANKLINE_MARKER
from turtle import width
import PySimpleGUI as sg
from armazenamento import armazenamento
from cpu import cpu
from tela_limpeza_disco import cleandisk
from img_tags import *

###função com janela de tarefas
def tela_tarefas():
    sg.theme('BlueMono')

    layout = [[sg.Text('Ferramentas',font='Helvetica 20 bold italic',text_color='black')],
              [sg.Text('Espaço  em disco         ',font='Helvetica 14 bold italic',text_color='white'),
              sg.Button('Verificar Espaço', image_data=image_large_rectangle,font='Helvetica 12 bold italic',
              button_color=('light blue',sg.theme_background_color()),border_width=0)],
              [sg.Text('Status do Processador',font='Helvetica 14 bold italic',text_color='white'),
              sg.Button('Verificar', image_data=image_large_rectangle,font='Helvetica 12 bold italic',key='process',
              button_color=('light blue',sg.theme_background_color()),border_width=0)],
              [sg.Text('Limpeza de Disco         ',font='Helvetica 14 bold italic',text_color='white'),
              sg.Button('Limpar de Disco',image_data=image_large_rectangle,font='Helvetica 12 bold italic',key='cleandisk',
              button_color=('light blue',sg.theme_background_color()),border_width=0)]]

    window = sg.Window('Tarefas',layout)

    while True:
        event, Values = window.read()
        if event == sg.WIN_CLOSED:
           break
        if event == 'Verificar Espaço':
            armazenamento()
        if event == 'process':
            cpu()
        if event == 'cleandisk':
            cleandisk()
    window.close()

