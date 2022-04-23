import os
import getpass
import pickle
import wget
import shutil

user = getpass.getuser()


def download(url, path, rmv=True, down=True):
    file_name = url.split('/')

    if down:
        wget.download(url)
    shutil.copyfile(os.getcwd() + '/' + file_name[-1], path + '/' + file_name[-1])
    if rmv:
        os.remove(os.getcwd() + '/' + file_name[-1])


if not os.path.exists('C:/Users/{}/AppData/Local/GEM Games/CodeRandom2/settings.pkl'.format(user)):
    new_settings = {
        'theme': 'THEME',
        'sfx volume': 1.0,
        'bgm volume': 0.8,
        'sfx muted': False,
        'bgm muted': False
        }
    with open('C:/Users/{}/AppData/Local/GEM Games/CodeRandom2/settings.pkl'.format(user), 'wb') as a:
        pickle.dump(new_settings, a)


def get(setting=None):
    print(setting)
    with open('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/settings.pkl', 'rb') as a:
        settings = pickle.load(a)
    if setting is not None:
        return settings[setting]
    else:
        return settings


def save(setting, value):
    settings = get()
    settings[setting] = value
    with open('C:/Users/{}/AppData/Local/GEM Games/CodeRandom2/settings.pkl'.format(user), 'wb') as a:
        pickle.dump(settings, a)

