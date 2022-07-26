import PySimpleGUI as sg
from img_tags import *
from armazenamento import *
from tela_select_site import select_site
from tela_tarefas import tela_tarefas
from tela_select_arquivos import select_arquivos
from tela_select_site import  select_site

def main():
    sg.theme('BlueMono')
    layout = [[sg.Button('', image_data=shield,
                         button_color=('light blue', sg.theme_background_color()), border_width=0),
               sg.Button('', image_data=UNIFESO,
                         button_color=('light blue', sg.theme_background_color()), border_width=0)]]

    layout += [[sg.Text('Verificar Site         ', font='Helvetica 16 bold italic', text_color='white'),
                sg.Button(' Selecionar site', image_data=image_large_rectangle, font='Helvetica 12 bold italic',
                          button_color=('light blue', sg.theme_background_color()), border_width=0,key='scanWebSite')],
               [sg.Text('Verificar Arquivo  ', font='Helvetica 16 bold italic', text_color='white'),
                sg.Button('Selecionar Arquivo', image_data=image_large_rectangle, font='Helvetica 12 bold italic',
                          button_color=('light blue', sg.theme_background_color()), border_width=0, )],
               [sg.Button('Ferramentas', image_data=image_large_rectangle, font='Helvetica 12 bold italic',key='ferramentas',
                          button_color=('light blue', sg.theme_background_color()), border_width=0, ),
                sg.Button('Configurações', image_data=image_large_rectangle, font='Helvetica 12 bold italic',
                          button_color=('light blue', sg.theme_background_color()), border_width=0, ), ],
               ]

    window = sg.Window('AllSafe Antivirus', layout)

    while True:
        event, Values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'scanWebSite':
            select_site()
        if event == 'ferramentas':
            # open janela
            tela_tarefas()
        if event == 'Selecionar Arquivo':
            #open janela
            select_arquivos();
    window.close()


main()
