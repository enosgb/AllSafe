import sys
import PySimpleGUI as sg
import os


def results(clean):
    sg.theme("BlueMono")
    clean = str(clean)
    
    layout = [[sg.Text('Nenhum virus detectado no arquivo informado.')],
                [sg.Button('Ok',key='ok')]]

    if clean == "False":
        sg.popup('Atenção! o site informado esta infectado com virus')  
        
    elif clean == "True":            
        sg.popup('o site informado é seguro')  
          