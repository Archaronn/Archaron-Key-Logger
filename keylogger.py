# $ pip3 install pynput

import pynput.keyboard

# listening - range

def order(letters):
    print(letters)

listening = pynput.keyboard.Listener(on_press=order)

with listening:
    listening.join()
