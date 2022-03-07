import PySimpleGUI as sg



def run():
    layout = [
        [sg.Multiline('', s=(30, 30))]
    ]

    return sg.Window('', layout, finalize=True)