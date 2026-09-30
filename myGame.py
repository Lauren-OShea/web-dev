import tetrisplayCUI
import time
import random

g = tetrisplayCUI.build_clean_grid()


from pynput import keyboard
 
key_pressed = None    # This is a global variable.
#full = False # making a global variable to check if the block is full or not

 
print("'a' key to move left, 'd' key to move right.")

def process_on_press(key):
    global key_pressed
    try:
        key_pressed = key.char
    except AttributeError:
        key_pressed = str(key)

while (key_pressed != "q"):
    listener = keyboard.Listener( on_press=process_on_press )

    listener.start()

    col = random.randint(0, tetrisplayCUI._COLUMNS - 1)

    for row in range(tetrisplayCUI._ROWS):  # gets key pressed and changes the block
        if(row == tetrisplayCUI._ROWS - 1):
            g = tetrisplayCUI.drop_block(g, col)
            tetrisplayCUI.display_grid(g)
            break
        
        elif tetrisplayCUI.block_full(g, col, row) == True:
            g = tetrisplayCUI.drop_block(g, col)
            break 
        
      
        if key_pressed:
            print(f"We got this key: {key_pressed}.")
            if key_pressed == "Key.left":
                if col >0: #if column is not empty
                    col = col-1
                    print("moved")
            
            if key_pressed == "Key.right":
                if col < tetrisplayCUI._COLUMNS - 1: #if column is not empty
                    col = col+1
                    print("moved")
            
            
            if key_pressed == "q":
                print("we're done.")
                break
        key_pressed = None
            
        tetrisplayCUI.show_dropping_block(g, col, row)
            
        listener.stop()

    if tetrisplayCUI.grid_full(g) == True:
        print("grid is full, game over.")
        break
   
    
     

   
