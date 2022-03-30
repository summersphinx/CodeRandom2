import getpass
import os
import random as r

import wget
from PySimpleGUI import popup_notify
from pygame import mixer

if os.getcwd().endswith('\\mods'):
    dir_path = os.getcwd()
else:
    dir_path = os.getcwd() + '/mods'

user = getpass.getuser()
songs = ['A Darker Kind Of Grid.mp3', 'Intro.mp3', 'Loading.mp3']

if not os.path.isdir('C:/Users/' + user + '/Music/GEM Games/CodeRandom/'):
    popup_notify('Getting Things Ready', title='Music', display_duration_in_ms=3000)
    os.makedirs('C:/Users/' + user + '/Music/GEM Games/CodeRandom/')

if len(os.listdir('C:/Users/' + user + '/Music/GEM Games/CodeRandom/')) <= 0:
    popup_notify('Setting the Stage', title='Music', display_duration_in_ms=3000)
    for each in songs:
        print(each)
        wget.download('https://github.com/summersphinx/CodeRandom-Stuff/raw/main/Music/' + each,
                      'C:/Users/' + user + '/Music/GEM Games/CodeRandom/' + each)

mixer.init()


class Music:
    music_path = 'C:/Users/' + user + '/Music/GEM Games/CodeRandom/'
    sfx_path = 'C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/'
    songs = os.listdir(music_path)

    def init(channel):
        return mixer.Channel(channel)

    def play(self):
        self.music.unload()
        self.music.play(r.choice(songs))

    def pause(self):
        self.pause()

    def stop(self):
        self.stop()

    def reload(self):
        songs = os.listdir()

        popup_notify('Reloaded Music', title='Music', display_duration_in_ms=2000)

    def volume(self, volume):
        self.volume(volume)

    def is_busy(self):
        return self.mixer.get_busy()
