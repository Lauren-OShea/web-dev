from typing import Text

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header, Static
from rich.text import Text
from pynput import keyboard

import tetrisplayCUI
import time
import random

CELL_W = 4
CELL_H = 2
COLOURS = ["red", "blue", "yellow", "green", "black", "purple"  ]


class GameScreen(Static, can_focus=True):
    
    
    key_pressed = None    # This is a global variable.
    #full = False # making a global variable to check if the block is full or not
    print("'Left Key' to move left, 'Right Key' to move right.")

    col = random.randint(0, tetrisplayCUI._COLUMNS - 1)
    row = 0
    
    """def process_on_press(key):
        global key_pressed
        try:
            key_pressed = key.char
        except AttributeError:
            key_pressed = str(key)"""

    def on_mount(self)-> None:
        """Method to start (or resume) time updating."""
        self.g = tetrisplayCUI.build_clean_grid()
        self.landed_colour = {}
        self.game_over = False
        self.new_block() 
        self.focus()
        self.timer = self.set_interval(0.5, self.tick)
        self.draw()

    def new_block(self)-> None:
        self.col = random.randint(0, tetrisplayCUI._COLUMNS - 1)
        self.row = 0
        self.block_colour = random.choice(COLOURS)
  
    def on_key(self, event: keyboard.Key) -> None:
        if self.game_over:
            return
        if event.key == "left" and self.col > 0:
            self.col -= 1
            print("moved left")
        elif event.key == "right" and self.col < tetrisplayCUI._COLUMNS - 1:
            self.col += 1
            print("moved right")
        self.draw()
   
    def tick(self)-> None:
        
        landed = (
            self.row>=tetrisplayCUI._ROWS - 1
            or tetrisplayCUI.block_full(self.g, self.col, self.row )
        )
        
        if landed:
            
            stacked_to_top = self.row == 0 
            self.g = tetrisplayCUI.drop_block(self.g, self.col)
            
            landed_row = self.g[self.col].index(tetrisplayCUI._BLOCK)
            self.landed_colour[self.col, landed_row] = self.block_colour
            
            if stacked_to_top or tetrisplayCUI.grid_full(self.g):
                self.game_over = True
                self.timer.stop()
                text = self.render_grid()
                text.append("\nGrid is full! Game Over :( )", style="bold red")
                self.draw()
                self.update(self.render_grid())
                
                return
            self.new_block()
        else:
            self.row += 1
            
        self.draw()
        
    def draw(self)-> None:
        self.update(self.render_grid())        
         
            
    def render_grid(self)-> Text:
        text = Text()
        for r in range(tetrisplayCUI._ROWS):
            for _ in range(CELL_H):
                text.append("|", style="white")
            for c in range(tetrisplayCUI._COLUMNS):
                if not self.game_over and r ==self.row and c == self.col:
                    style = f"on {self.block_colour}"
                elif self.g[c][r] == tetrisplayCUI._BLOCK:
                    style = f"on {self.landed_colour.get((c, r), 'blue')}"
                else:
                    style = ""
                text.append(" " * CELL_W, style=style)
                text.append("|", style="white")
            text.append("\n")
        return text

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
     

   
