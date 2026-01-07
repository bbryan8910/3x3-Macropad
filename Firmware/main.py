import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.D1, board.D2, board.D3)  # Column0, Column1, Column2
keyboard.row_pins = (board.D4, board.D6, board.D7)  # Row0, Row1, Row2
keyboard.diode_orientation = 'COL2ROW'

keyboard.keymap = [
    [
        # Top row 
        KC.F13,                             
        KC.F14,
        KC.F15,
        
        # Middle row 
        KC.F16,
        KC.F17,              
        KC.F18,                            
        
        # Bottom row 
        KC.AUDIO_VOL_DOWN,
        KC.AUDIO_MUTE,
        KC.AUDIO_VOL_UP,
    ]
]

if __name__ == '__main__':
    keyboard.go()
