import tkinter as tk
from game_of_life import GameOfLife
from cell import CellStates
import time
square_size = 30

class GUI:

    def __init__(self, game_of_life, root, canvas):
        self.game = game_of_life
        self.root = root
        self.canvas = canvas
        
    def start(self):
        self.render_cells()
        self.root.mainloop()
    
    def render_cells(self):

        cells = self.game.cells

        for pos in cells:
            row, col = pos
            self.canvas.create_rectangle(
                row * square_size,
                col * square_size,
                row * square_size + square_size,
                col * square_size + square_size,
                fill="black" if cells[pos].is_alive else "white"
            )

        self.game.tick()
        self.root.after(1000, self.render_cells)


def init_board():
    game = GameOfLife()

    game.add_cell(0,0,CellStates.ALIVE)
    game.add_cell(0,1,CellStates.DEAD)
    game.add_cell(0,2,CellStates.DEAD)
    game.add_cell(0,3,CellStates.DEAD)

    game.add_cell(1,0,CellStates.DEAD)
    game.add_cell(1,1,CellStates.ALIVE)
    game.add_cell(1,2,CellStates.ALIVE)
    game.add_cell(1,3,CellStates.ALIVE)

    game.add_cell(2,0,CellStates.ALIVE)
    game.add_cell(2,1,CellStates.ALIVE)
    game.add_cell(2,2,CellStates.ALIVE)
    game.add_cell(2,3,CellStates.DEAD)

    game.add_cell(3,0,CellStates.ALIVE)
    game.add_cell(3,1,CellStates.DEAD)
    game.add_cell(3,2,CellStates.DEAD)
    game.add_cell(3,3,CellStates.DEAD)
    return game



def main():
    game = init_board()
    root = tk.Tk()
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()
    
    gui = GUI(game, root, canvas)
    gui.start()
    

if __name__ == "__main__":
    main()