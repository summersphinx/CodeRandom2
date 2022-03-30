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
