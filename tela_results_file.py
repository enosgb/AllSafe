import sys
import PySimpleGUI as sg
import os


def results(clean,filepath):
    sg.theme("BlueMono")
    clean = str(clean)
    path = filepath
    def keepFile():
        sg.popup('o arquivo foi mantido.')
        print('deseja manter o arquivo')


    def removeFile(filename):
        os.remove(filename)
        sg.popup('o arquivo foi removido.') 

    layout = [[sg.Text('Nenhum virus detectado no arquivo informado.')],
                [sg.Button('Ok',key='ok')]]

    if clean == "False":
        layout = [[sg.Text('Atenção o arquivo selecionado esta infectado')],
                [sg.Button('Manter arquivo',key='keepFile'), sg.Button('Remover Arquivo',key='removeFile')]]
        window = sg.Window('Resultado', layout)

        while True:             # Event Loop
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'keepFile':
                keepFile()
                break        # call the "Callback" function
            elif event == 'removeFile':
                removeFile(path)        # call the "Callback" function
                break
            elif event == 'ok':
                break
        window.close()    
        
    elif clean == "True":            
        layout = [[sg.Text('Nenhum virus detectado no arquivo informado.')],
                [sg.Button('Ok',key='ok')]]
        window = sg.Window('Resultado', layout)

        while True:             # Event Loop
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'keepFile':
                keepFile()        # call the "Callback" function
            elif event == 'removeFile':
                removeFile()        # call the "Callback" function
            elif event == 'ok':
                break
        window.close()        
    
