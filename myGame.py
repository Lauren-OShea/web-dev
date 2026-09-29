import tetrisplayCUI
import time

g = tetrisplayCUI.build_clean_grid()
tetrisplayCUI.display_grid(g)
tetrisplayCUI.show_dropping_block(g, 1)
from pynput import keyboard
 
key_pressed = None    # This is a global variable.


 
print("'a' key to move left, 'd' key to move right.")

def process_on_press(key):
    global key_pressed
    try:
        key_pressed = key.char
    except AttributeError:
        key_pressed = str(key)


listener = keyboard.Listener( on_press=process_on_press )

listener.start()

while True:
    if key_pressed:
        print(f"We got this key: {key_pressed}.")
        if key_pressed == "a":
            print("moved")
            break
        key_pressed = None

    print(tetrisplayCUI.display_grid(tetrisplayCUI.build_clean_grid()))
    time.sleep(0.5)


listener.stop()

