import tetrisplayCUI
import time
import random

g = tetrisplayCUI.build_clean_grid()


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

col = random.randint(0, tetrisplayCUI._COLUMNS - 1)

for row in range(tetrisplayCUI._ROWS):  # gets key pressed and changes the block 
    if key_pressed:
        print(f"We got this key: {key_pressed}.")
        if key_pressed == "a":
            col = col-1
            print("moved")
        
        if key_pressed == "d":
            col = col+1
            print("moved")
        
        
        if key_pressed == "q":
            print("we're done.")
            break
       
        
        key_pressed = None
    tetrisplayCUI.show_dropping_block(g, col, row)

if(row == tetrisplayCUI._ROWS - 1):
    g = tetrisplayCUI.drop_block(g, col)
    tetrisplayCUI.display_grid(g)



listener.stop()
