from pygame import mixer
import random as r
import getpass
import zipfile
import wget
import os
from shutil import copytree, rmtree
from PySimpleGUI import popup_notify

if os.getcwd().endswith('\\mods'):
    dir_path = os.getcwd()
else:
    dir_path = os.getcwd() + '/mods'

user = getpass.getuser()

url = 'https://github.com/summersphinx/CodeRandom2/raw/main/mods/bg.zip'

if not os.path.isdir('C:/Users/' + user + '/Music/GEM Games/CodeRandom/'):
    popup_notify('Getting Things Ready', title='Music', display_duration_in_ms=3000)
    wget.download(url)
    zipfile.is_zipfile(dir_path + '/bg.zip')
    with zipfile.ZipFile(dir_path + '/bg.zip', 'r') as ZIP:
        ZIP.printdir()
        ZIP.extractall()
    copytree(dir_path + '/bg', 'C:/Users/' + user + '/Music/GEM Games/CodeRandom/')
    os.remove(dir_path + '/bg.zip')
    rmtree(dir_path + '/bg')

mixer.init()


def init(channel):
    return mixer.Channel(channel)


songs = os.listdir('C:/Users/' + user + '/Music/GEM Games/CodeRandom/')
print(songs)


def shuffle(channel):
    channel.music.unload()
    channel.music.play(r.choice(songs))


def play(channel):
    channel.music.play()


def pause(channel):
    channel.music.pause()


def quit(channel):
    channel.quit()


def volume(channel, *v):
    try:
        vol = v[0]
        channel.set_volume(vol / 10)
    except IndexError:
        return channel.get_volume()


def music():
    return os.listdir('C:/Users/' + user + '/Music/CodeRandom/')


test = init(0)
print(volume(test))
volume(test, 12)
print(volume(test))
