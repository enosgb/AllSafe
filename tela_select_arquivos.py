from tokenize import String
import PySimpleGUI as sg
from api_virus import scanningFile;
from tela_results_file import results;

###criando tela de verificação de arquivos
pathGlobal = ''

def selectfile(filename):
    filepath = filename
    #filepath =  filepath.replace('/','\\\\')
    clean = scanningFile(filepath)
    results(clean,filepath)

def select_arquivos():
    filename = sg.popup_get_file('Selecione um arquivo para Verificação', title='selecione um arquivo')

    if filename:
        selectfile(filename)
    else:
        sg.popup_cancel('Nenhum arquivo valido foi selecionado')

