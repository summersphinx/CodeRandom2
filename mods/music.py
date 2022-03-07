from pygame import mixer
import random as r
import getpass
import zipfile
import wget
import os

user = getpass.getuser()

url = 'https://www.mediafire.com/file/ik6hn0bub76crcl/bg.zip/file'

# , 'C:/Users/' + user + '/Music/CodeRandom/bg.zip'
wget.download(url)
zipfile.is_zipfile(os.getcwd() + '/bg.zip')
with zipfile.ZipFile(os.getcwd() + '/bg.zip', 'r') as zip:
    zip.printdir()
    zip.extractall()


mixer.init()


def shuffle(channel):
    mixer.music.unload()


def play(channel):
    mixer.music.play()


def pause(channel):
    mixer.music.pause()


def quit():
    mixer.quit()


def volume(channel, *v):
    try:
        vol = v[0]
        mixer.music.set_volume(vol / 10)
    except IndexError:
        return mixer.music.get_volume()
