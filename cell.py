
class CellStates:
    ALIVE = "alive"
    DEAD = "dead"
    POSSIBLE_STATES = [ALIVE, DEAD]

class Cell:
    def __init__(self, game_of_life, row, col, state):
        if state not in CellStates.POSSIBLE_STATES:
            raise ValueError(f"Invalid state [{state}] provided.")

        self.game_of_life = game_of_life
        self.row = row
        self.col = col
        self.state = state

    @property
    def neighbours(self):
        return self.game_of_life.get_cell_neighbours(self)

    @property
    def live_neighbours(self):
        return [cell for cell in self.neighbours if cell.is_alive]

    @property
    def is_alive(self):
        return self.state == CellStates.ALIVE

    def die(self):
        self.state = CellStates.DEAD

    def resurrect(self):
        self.state = CellStates.ALIVE

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Cell(row={self.row}, col={self.col}, state={self.state})"