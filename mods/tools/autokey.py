import string
from pycipher import Caesar as C
import PySimpleGUI as sg




def run():
    table_b = []
    upper_char = list(string.ascii_uppercase)
    iteration = 0

    for i in string.ascii_uppercase:
        table_b.append([upper_char[iteration]] + list(C(iteration).encipher(string.ascii_lowercase).lower()))
        iteration += 1

    notes_layout = [[sg.Frame('', [
        [sg.Table(table_b, num_rows=27, vertical_scroll_only=False, hide_vertical_scroll=True, auto_size_columns=False,
                  col_widths=[2] * 27, headings=[' '] + list(string.ascii_uppercase))]])]]

    autokey_wn = sg.Window('Autokey Table', notes_layout, finalize=True)
    return autokey_wn.read()

