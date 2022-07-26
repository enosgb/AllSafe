import PySimpleGUI as sg
import base64

###criando tela de verificação de arquivos

def convert_file_to_base64(filename):
    '''
    try:
        contents = open(filename, 'rb').read()
        encoded = base64.b64encode(contents)
        sg.clipboard_set(encoded)
        # pyperclip.copy(str(encoded))
        sg.popup('Copied to your clipboard!', 'Keep window open until you have pasted the base64 bytestring')
    except Exception as error:
        sg.popup_error('Cancelled - An error occurred', error)'''
    print(filename);

def select_arquivos():
    filename = sg.popup_get_file('Selecione um arquivo para Verificação', title='selecione um arquivo')

    if filename:
        convert_file_to_base64(filename)
    else:
        sg.popup_cancel('Nenhum arquivo valido foi selecionado')

