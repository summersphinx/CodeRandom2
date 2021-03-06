import getpass
import os
from PySimpleGUI import popup_notify
from shutil import copytree, rmtree
import wget
import shutil
from datetime import date
import zipfile


def download(url, path, rmv=True, down=True):
    file_name = url.split('/')

    if down:
        wget.download(url)
    shutil.copyfile(os.getcwd() + '/' + file_name[-1], path + '/' + file_name[-1])
    if rmv:
        os.remove(os.getcwd() + '/' + file_name[-1])


if os.getcwd().endswith('\\mods'):
    dir_path = os.getcwd()
else:
    dir_path = os.getcwd() + '/mods'

user = getpass.getuser()

# 'C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2'

if not os.path.isdir('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2'):
    print("Running")

    os.makedirs('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2')
    print("DIR Made")

    popup_notify('Getting Things Ready', title='Game', display_duration_in_ms=3000)
    download('https://github.com/summersphinx/CodeRandom-Stuff/raw/main/words_alpha.txt', 'C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2')
    a = open('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/last_day.txt'.format(user=user), 'w')
    a.write(str(date.today()))
    a.close()

else:
    with open('C:/Users/' + user + "/AppData/Local/GEM Games/CodeRandom2/last_day.txt") as a:
        if a.read() != str(date.today()):
            popup_notify('Getting Things Ready', title='Game', display_duration_in_ms=3000)
            download('https://github.com/summersphinx/CodeRandom-Stuff/raw/main/words_alpha.txt', 'C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2')
            a = open('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/last_day.txt', 'w')
            a.write(str(date.today()))
            a.close()

songs = ['A Darker Kind Of Grid.mp3', 'Intro.mp3', 'Loading.mp3']

if not os.path.isdir('C:/Users/' + user + '/Music/GEM Games/CodeRandom/'):
    popup_notify('Getting Things Ready', title='Music', display_duration_in_ms=3000)
    os.makedirs('C:/Users/' + user + '/Music/GEM Games/CodeRandom/')

if len(os.listdir('C:/Users/' + user + '/Music/GEM Games/CodeRandom/')) <= 0:
    popup_notify('Setting the Stage', title='Music', display_duration_in_ms=3000)
    for each in songs:
        wget.download('https://github.com/summersphinx/CodeRandom-Stuff/raw/main/Music/' + each,
                      'C:/Users/' + user + '/Music/GEM Games/CodeRandom/' + each)

sounds = ['lose.wav', 'menu.wav', 'settings.wav', 'start.wav', 'win.wav']

if not os.path.isdir('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/'):
    popup_notify('Getting Things Ready', title='Music', display_duration_in_ms=3000)
    os.makedirs('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/')

if len(os.listdir('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/')) <= 0:
    popup_notify('Getting the Special Stuff', title='Sound', display_duration_in_ms=3000)
    for each in sounds:
        wget.download('https://github.com/summersphinx/CodeRandom-Stuff/raw/main/2/sfx/' + each, 'C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/' + each)
