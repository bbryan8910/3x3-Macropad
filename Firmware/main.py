import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.AUDIO_VOL_DOWN, KC.AUDIO_MUTE, KC.AUDIO_VOL_UP]
]

if __name__ == '__main__':
    keyboard.go()
