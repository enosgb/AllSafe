import PySimpleGUI as sg
from tela_results_web import results
from api_virus_web import scanningWebSite


def select_site():
    url = sg.popup_get_text('Informe a url do site para verificação',
    title='Verificando seguranca do site')
    if(url != None):
        clean = scanningWebSite(url)
        results(clean)