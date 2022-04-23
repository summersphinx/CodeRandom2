import pickle
import os
import getpass

path = 'C:/Users/' + getpass.getuser() + '/Music/GEM Games/CodeRandom/'

print(path)

class encrypt:
    def __init__(self):
        for each in os.listdir(path):
            with open(path + each, 'wb') as a:
                pickle.dump(a, a)

print(path)

class decrypt:
    def __init__(self):
        for each in os.listdir(path):
            with open(path + each, 'wb') as a:
                pickle.load(a)

print(path)

encrypt.__init__('')