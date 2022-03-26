import urllib3
from socket import gethostname
import PySimpleGUI as sg
import requests

http = urllib3.PoolManager()


def get(*dev):
    try:
        if dev[0]:
            grabbed_levels = http.request('GET', 'https://raw.githubusercontent.com/summersphinx/CodeRandom-Stuff/main/2/levels.txt')
        else:
            grabbed_levels = http.request('GET', 'https://raw.githubusercontent.com/summersphinx/CodeRandom-Stuff/main/2/levels.txt')
        return eval(grabbed_levels.data)
    except IndexError:
        h_name = gethostname()
        dev = False
        if h_name == 'msi-gavin':
            if sg.PopupYesNo('Use Dev Levels?') == 'Yes':
                dev = True
        return dev


def levels(dictionary):
    names = []
    for key in dictionary.keys():
        names.append(key)
    return names
