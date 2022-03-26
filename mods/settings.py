import os
import getpass
import pickle

user = getpass.getuser()


def get(setting=None):
    print(setting)
    with open('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/data.save') as a:
        settings = eval(a.read())
    if setting is not None:
        return settings[setting]
    else:
        return settings


def save():
    settings = get()
