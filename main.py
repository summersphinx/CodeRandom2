import random as r
import time
import webbrowser
import getpass

import PySimpleGUI as sg
import urllib3

import mods.cipher as cipher
import mods.levels as levels
import mods.load_words as load_words
import mods.tools.autokey as autokey
import mods.tools.notepad as notepad
import mods.tools.tap as tap
import mods.download
import mods.music as music

# Get Profile Name
user = getpass.getuser()



# Music Channels
bg = music.init(0)
sfx = music.init(1)

music.volume(sfx, )

# Set up Web Browser
http = urllib3.PoolManager()

# Set Theme for Window
sg.theme('DarkGrey14')

# Define the title bar for the Window
titleBar = [['Music', ['Mute', 'Mixer']], ['Settings', ['Menu', 'About', 'Quit']]]

# Menu Layouts

dev = levels.get()
level_names = levels.get(dev)

menu_layout_left = [
    [sg.Frame('Play', [[sg.Listbox(levels.levels(level_names), s=(24, 10), default_values='Intro', k='level_select')],
                       [sg.Text('')], [sg.Button('Play', s=(25, 2))]], s=(320, 480))]
]

menu_layout_right = [
    [sg.Frame('Play More', [[sg.Text('WIP')]], s=(320, 480))]
]

menu_layout = [
    [sg.Column(menu_layout_left),
     sg.Column(menu_layout_right)]
]

# Puzzle Layouts

tool_layout = [
    [sg.Button('NotePad')],
    [sg.Button('ScratchPad', disabled=not dev)],
    [sg.Text('')],
    [sg.Button('Autokey Table')],
    [sg.Button('Tap Code')]
]

layout_puzzle_left = [
    [sg.Frame('Encrypted Word', [[sg.Text('', justification='center', s=(390, 60), k='puzzle')]], s=(400, 70))],
    [sg.Frame('Guess', [[sg.Input('', s=(14, 1), k='guess'), sg.Button('Test', font='Veranda 14')]], s=(400, 70))],
    [sg.Frame('Steps', [[sg.Multiline('', disabled=True, s=(390, 330), k='hints')]], s=(400, 340))]
]

layout_puzzle_right = [
    [sg.Frame('Tools', tool_layout, s=(240, 470))]
]

puzzle_layout = [
    [sg.Column(layout_puzzle_left),
     sg.Column(layout_puzzle_right)]
]

sg.theme('DarkGreen1')
win_layout = [
    [sg.Frame('',
              [[sg.Text('You Win!', font='Veranda 48 bold')], [sg.Text('')], [sg.Button('Menu')], [sg.Button('Quit')]],
              s=(630, 470), element_justification='center')]]

sg.theme('DarkGrey14')
layout = [
    [sg.Menu(titleBar)],
    [sg.Column(menu_layout, k='m'),
     sg.Column(puzzle_layout, k='p'),
     sg.Column(win_layout, k='w', visible=False)]
]

# Create the Window
wn = sg.Window('CodeRandom2', layout, size=(640, 480), font='Veranda 16', finalize=True)

while True:
    window, event, values = sg.read_all_windows()

    if window == wn:

        if event in (None, 'Quit'):
            break
        if event == 'Menu':
            wn['m'].Update(visible=True)
            wn['p'].Update(visible=False)
            wn['w'].Update(visible=False)
            hints = ''
            wn['hints'].Update(value=hints)
        if event == 'Play':
            wn['m'].Update(visible=False)
            wn['p'].Update(visible=True)
            start_time = int(time.time())

            master_word = r.choice(load_words.load_words(5))
            steps = level_names[values['level_select'][0]]

            iteration = 0
            master_encrypted = master_word
            print(master_word)
            hints = ''
            for step in steps:
                word = r.choice(load_words.load_words(4))
                hints += values['hints'] + word + '   ->   ' + cipher.encrypt(step, word) + '\n'
                wn['hints'].Update(value=hints)
                master_encrypted = cipher.encrypt(step, master_encrypted)

            wn['puzzle'].Update(value=master_encrypted)
        if event == 'Test':
            if master_word == values['guess'].lower():
                wn['m'].Update(visible=False)
                wn['p'].Update(visible=False)
                wn['w'].Update(visible=True)
                hints = ''
                wn['hints'].Update(value=hints)
                wn['guess'].Update(value=hints)

        if event == 'About':
            webbrowser.open('https://gemgames.w3spaces.com/CodeRandom2/help.html')
        if event == 'Autokey Table':
            autokeyTable = autokey.run()
        if event == 'Tap Code':
            tapCode = tap.run()
        if event == 'NotePad':
            notes = notepad.run()

    try:
        if window == notes:

            if event in (None, 'Quit'):
                notes.close()
    except NameError:
        try:
            if window == autokeyTable:

                if event in (None, 'Quit'):
                    autokeyTable.close()
        except NameError:
            try:
                if window == tapCode:

                    if event in (None, 'Quit'):
                        tapCode.close()
            except NameError:
                pass

wn.close()
