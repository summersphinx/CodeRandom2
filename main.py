import getpass
import random as r
import time
import traceback
import webbrowser
import pyperclip
import urllib3
import os

import pygame.mixer as music
import PySimpleGUI as sg

sg.SetGlobalIcon('E:/Github/CodeRandom2/favicon.ico')

import mods.download
import mods.cipher as cipher
import mods.levels as levels
import mods.load_words as load_words
import mods.tools.autokey as autokey
import mods.tools.notepad as notepad
import mods.tools.tap as tap
import mods.settings as Settings

print(Settings.get())

music.init()

try:

    # Get Profile Name
    user = getpass.getuser()

    # Music Paths
    bgm = ('C:/Users/{}/Music/GEM Games/CodeRandom/'.format(user))

    # Music Channels
    bg = music.Channel(0)
    sfx = music.Channel(1)

    bg.set_volume(Settings.get('bgm volume'))
    sfx.set_volume(Settings.get('sfx volume'))

    if Settings.get('bgm muted'):
        bg.set_volume(0)
    if Settings.get('sfx muted'):
        sfx.set_volume(0)

    bg.play(music.Sound(bgm + r.choice(os.listdir(bgm))))

    # Set up Web Browser
    http = urllib3.PoolManager()

    sg.theme('DarkGreen1')
    win_layout = [
        [sg.Frame('',
                  [[sg.Text('You Win!', font='Veranda 48 bold')], [sg.Text('')], [sg.Button('Menu')],
                   [sg.Button('Quit')]],
                  s=(630, 470), element_justification='center')]]

    # Set Theme for Window
    sg.theme(Settings.get('theme'))

    # Define the title bar for the Window
    titleBar = [['Music', ['Mute', 'Mixer']], ['Settings', ['Menu', 'About', 'Credits', 'Quit']]]

    # Mixer Layouts

    mixer_layout = [
        [sg.Text('BG Music')],
        [sg.Slider(range=(0, 1), k='bgm volume', resolution=0.01, orientation='h', default_value=Settings.get('bgm volume'))],
        [sg.Text('Mute'), sg.Checkbox('', Settings.get('bgm muted'), k='bgm muted')],
        [sg.Text('\n\n')],
        [sg.Text('SFX')],
        [sg.Slider(range=(0, 1), k='sfx volume', resolution=0.01, orientation='h', default_value=Settings.get('sfx volume'))],
        [sg.Text('Mute'), sg.Checkbox('', Settings.get('sfx muted'), k='sfx muted')],
        [sg.Button('Save', k='SaveSettings')]
    ]

    # Menu Layouts

    dev = levels.get()
    level_names = levels.get(dev)

    menu_layout_left = [
        [sg.Frame('Play',
                  [[sg.Listbox(levels.levels(level_names), s=(24, 10), default_values=['Intro'], k='level_select')],
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

    # Puzzle Layouts

    layout_puzzle_left = [
        [sg.Frame('Encrypted Word', [[sg.Text('', justification='center', s=(390, 60), k='puzzle')]], s=(400, 70))],
        [sg.Frame('Guess',
                  [[sg.Input('', s=(14, 1), k='guess'), sg.Button('Test', font='Veranda 14'), sg.Button('Give Up', )]],
                  s=(400, 70))],
        [sg.Frame('Steps', [[sg.Multiline('', disabled=True, s=(390, 330), k='hints')]], s=(400, 340))]
    ]

    layout_puzzle_right = [
        [sg.Frame('Tools', tool_layout, s=(240, 470))]
    ]

    puzzle_layout = [
        [sg.Column(layout_puzzle_left),
         sg.Column(layout_puzzle_right)]
    ]

    # Combine layouts into one layout for window

    layout = [
        [sg.Menu(titleBar)],
        [sg.Column(menu_layout, k='m'),
         sg.Column(puzzle_layout, k='p', visible=False),
         sg.Column(win_layout, k='w', visible=False),
         sg.Column(mixer_layout, k='s', visible=False)]
    ]

    # Create the Window
    wn = sg.Window('CodeRandom2', layout, size=(640, 480), font='Veranda 18', finalize=True)

    while True:

        # Read window, or check for update with bgm
        window, event, values = sg.read_all_windows(timeout=20000, timeout_key='REFRESH')

        # Check if bgm is playing
        if event == 'REFRESH':
            if not bg.get_busy():
                bg.play(music.Sound(bgm + r.choice(os.listdir(bgm))))

        if event != 'REFRESH':
            print(window)
            print(event)
            print(values)
            print('')

        if window == wn:

            # Close Windows
            if event in (None, 'Quit'):
                break
            if event == 'Mixer':
                wn['m'].Update(visible=False)
                wn['p'].Update(visible=False)
                wn['w'].Update(visible=False)
                wn['s'].Update(visible=True)

            if event == 'Menu':
                # Switch to main menu layout
                sfx.play(music.Sound('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/menu.wav'))
                wn['m'].Update(visible=True)
                wn['p'].Update(visible=False)
                wn['w'].Update(visible=False)
                wn['s'].Update(visible=False)
                hints = ''
                wn['hints'].Update(value=hints)
            if event == 'SaveSettings':
                # Switch to main menu layout
                sfx.play(music.Sound('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/menu.wav'))
                wn['m'].Update(visible=True)
                wn['p'].Update(visible=False)
                wn['w'].Update(visible=False)
                wn['s'].Update(visible=False)

                sfx_volume = values['sfx volume']

                Settings.save('sfx volume', values['sfx volume'])
                Settings.save('bgm volume', values['bgm volume'])
                Settings.save('sfx muted', values['sfx muted'])
                Settings.save('bgm muted', values['bgm muted'])

                bg.set_volume(Settings.get('bgm volume'))
                sfx.set_volume(Settings.get('sfx volume'))

                if Settings.get('bgm muted'):
                    bg.set_volume(0)
                if Settings.get('sfx muted'):
                    sfx.set_volume(0)

            if event == 'Play':

                # Create Puzzle from level data
                if len(values['level_select']) != 0:
                    sfx.play(music.Sound('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/start.wav'))
                    wn['m'].Update(visible=False)
                    wn['p'].Update(visible=True)
                    wn['s'].Update(visible=False)
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
                else:
                    sfx.play(music.Sound('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/menu.wav'))
                    sg.PopupOK('No Level Selected')
            if event == 'Test':
                # Test user guess against master word
                # noinspection PyUnboundLocalVariable
                if master_word == values['guess'].lower():
                    sfx.play(music.Sound('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/win.wav'))
                    wn['m'].Update(visible=False)
                    wn['p'].Update(visible=False)
                    wn['w'].Update(visible=True)
                    wn['s'].Update(visible=False)
                    hints = ''
                    wn['hints'].Update(value=hints)
                    wn['guess'].Update(value=hints)
                else:
                    sfx.play(music.Sound('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/lose.wav'))

            if event == 'About':
                # Open about page in browser
                sfx.play(music.Sound('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/menu.wav'))
                webbrowser.open('https://gemgames.w3spaces.com')
            if event == 'Credits':
                # Open about page in browser
                sfx.play(music.Sound('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/menu.wav'))
                webbrowser.open('https://gemgames.nicepage.io/CodeRandom/Credits.html')
            if event == 'Autokey Table':
                autokeyTable = autokey.run()
            if event == 'Tap Code':
                tapCode = tap.run()
            if event == 'NotePad':
                notes = notepad.run()

        try:
            # noinspection PyUnboundLocalVariable
            if window == notes:

                if event in (None, 'Quit'):
                    notes.close()
        except NameError:
            try:
                # noinspection PyUnboundLocalVariable
                if window == autokeyTable:

                    if event in (None, 'Quit'):
                        autokeyTable.close()
            except NameError:
                try:
                    # noinspection PyUnboundLocalVariable
                    if window == tapCode:

                        if event in (None, 'Quit'):
                            tapCode.close()
                except NameError:
                    pass

    sfx.play(music.Sound('C:/Users/' + user + '/AppData/Local/GEM Games/CodeRandom2/sfx/menu.wav'))
    wn.close()

except Exception as e:
    if sg.PopupYesNo(
            'An Error Occurred, would you like to \nauto report this Error?\n\n' + traceback.format_exc() + '\n\nThe error message will be copied to the clipboard.',
            title='Error') == 'Yes':
        pyperclip.copy(traceback.format_exc())

        webbrowser.open('https://forms.gle/4P1vP6hjp9aBh3SS7')
