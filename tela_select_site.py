import PySimpleGUI as sg


def select_site():
    filename = sg.popup_get_text('Informe a url do site para verificação',
    title='Verificando seguranca do site')
    print(filename);