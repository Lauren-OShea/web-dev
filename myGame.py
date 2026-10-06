from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header, Static

import tetrisplayCUI
import time
import random

class GameScreen(Static):
    
    from pynput import keyboard
    key_pressed = None    # This is a global variable.
    #full = False # making a global variable to check if the block is full or not
    print("'Left Key' to move left, 'Right Key' to move right.")

    
    def process_on_press(key):
        global key_pressed
        try:
            key_pressed = key.char
        except AttributeError:
            key_pressed = str(key)

    def on_mount(self):
        """Method to start (or resume) time updating."""
        self.g = tetrisplayCUI.build_clean_grid()
        #self.start_time = monotonic()
        #self.update_timer.resume()

    def move(self):
     """Method to move blocks
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
            
           
        key_pressed = None
            
        tetrisplayCUI.show_dropping_block(self.g, col, row)
            

        while (key_pressed != "q"):
            listener = keyboard.Listener( on_press=process_on_press )

            listener.start()

            col = random.randint(0, tetrisplayCUI._COLUMNS - 1)

            for row in range(tetrisplayCUI._ROWS):  # gets key pressed and changes the block
                if(row == tetrisplayCUI._ROWS - 1):
                    self.g = tetrisplayCUI.drop_block(self.g, col)
                    tetrisplayCUI.display_grid(self.g)
                    break
                
                elif tetrisplayCUI.block_full(self.g, col, row) == True:
                    self.g = tetrisplayCUI.drop_block(self.g, col)
                    break 
                
            
            listener.stop()

            if tetrisplayCUI.grid_full(self.g) == True:
                print("grid is full, game over.")
                break"""
        
class TetrisApp(App):
    CSS_PATH = "myGame.tcss"
    
    BINDINGS = [
        ("q", "quit", "Quit")#,
        #("left", "Key.left", "<-"),
        #("right", "Key.right", "#"),
        ]
    

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        with HorizontalGroup():
            yield GameScreen()
        yield Footer()
       

    
if __name__ == "__main__":
    app = TetrisApp()
    app.run()
     

   
