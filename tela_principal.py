from cgitb import text
from tkinter import font
import PySimpleGUI as sg
from img_tags import *
from armazenamento import *



sg.theme('BlueMono')
layout = [[sg.Button('', image_data=shield, button_color=('light blue', sg.theme_background_color()),
                      border_width=0, ),sg.Text('Drive Status', font='Helvetica 16 bold italic',text_color='white')]]

                      
layout += [[sg.Text('Full Scan               ',font='Helvetica 16 bold italic',text_color='white'),sg.Button(' Iniciar Verificação', image_data=image_large_rectangle,font='Helvetica 12 bold italic', button_color=('light blue', sg.theme_background_color()),
                      border_width=0, )],
         [sg.Text('Verificar Arquivo  ',font='Helvetica 16 bold italic',text_color='white'),sg.Button('Selecionar Arquivo', image_data=image_large_rectangle, font='Helvetica 12 bold italic', button_color=('light blue', sg.theme_background_color()),
                      border_width=0, )],
         [sg.Button('Tarefas', image_data=image_large_rectangle, font='Helvetica 12 bold italic', button_color=('light blue', sg.theme_background_color()),
                      border_width=0, ),sg.Button('Configurações', image_data=image_large_rectangle, font='Helvetica 12 bold italic', button_color=('light blue', sg.theme_background_color()),
                      border_width=0, ),],
         
]
'''
particians = psutil.disk_partitions()
for count, part in enumerate(particians):
    mount = part[0]
    try:
        bar_color = sg.theme_progress_bar_color()
        this_color = BAR_COLORS[count % len(BAR_COLORS)]
        usage = psutil.disk_usage(mount)
        stats_info = f'{human_size(usage.used)} / {human_size(usage.total)} = {human_size(usage.free)} free'
        layout += [[sg.Text(mount, size=(5, 1), key=('-NAME-', mount)),
                    sg.ProgressBar(100, 'h', size=(10, 15), key=('-PROG-', mount), bar_color=(this_color, bar_color[1])),
                    sg.Text(f'{usage.percent}%', size=(6, 1), key=('-%-', mount)), sg.T(stats_info, size=(30, 1), key=('-STATS-', mount))]]
    except:
        pass
    layout += [[sg.Text('Refresh', font='Any 8', key='-REFRESH-', enable_events=True), sg.Text('❎', enable_events=True, key='Exit Text')]]
'''

window = sg.Window('AllSafe Antivirus',layout)

while True:
    event, Values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()