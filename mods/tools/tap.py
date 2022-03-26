import PySimpleGUI as sg




def run():
    table = '''
      A | B |C/K| D | E 
     ---+---+---+---+---
      F | G | H | I | J
     ---+---+---+---+---
      L | M | N | O | P 
     ---+---+---+---+---
      Q | R | S | T | U
     ---+---+---+---+---
      V | W | X | Y | Z
    '''

    notes_layout = [[sg.Text(table)]]

    return sg.Window('Tap Code', notes_layout, finalize=True)
