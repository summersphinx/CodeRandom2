import shutil
import PySimpleGUI as sg
import getpass
import os

user = getpass.getuser()

test = sg.PopupOKCancel("Are you sure you want to repair?", title='CodeRandom2 - Repair')
print(test)
if test == 'OK':
    if os.path.isdir('C:/Users/' + user + '/Music/GEM Games/CodeRandom'):
        shutil.rmtree('C:/Users/' + user + '/Music/GEM Games/CodeRandom')
    if os.path.isdir('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2'):
        shutil.rmtree('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2')

    sg.PopupOK('Done!', title='CodeRandom2 - Repair')
else:
    sg.PopupOK('Repair Cancelled!', title='CodeRandom2 - Repair')
