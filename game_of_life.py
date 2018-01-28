from cell import Cell

class GameOfLife:
    def __init__(self, cells=None):
        self.cells = cells if cells else {}
    
    def add_cell(self, row, col, state):
        cell = Cell(self, row, col, state)
        self.cells[(row, col)] = cell
        return cell

    def get_cell(self, row, col):
        return self.cells.get((row, col))

    def tick(self):

        # 1) Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
        cells_to_die = [cell for cell in self.cells.values() if cell.is_alive and len(cell.live_neighbours) < 2]
        
        # 2) Any live cell with two or three live neighbours lives on to the next generation.
        # no code needed.

        # 3) Any live cell with more than three live neighbours dies, as if by overpopulation.
        cells_to_die.extend([cell for cell in self.cells.values() if cell.is_alive and len(cell.live_neighbours) > 3])

        # 4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        cells_to_resurrect = [cell for cell in self.cells.values() if not cell.is_alive and len(cell.live_neighbours) == 3]

        for cell in cells_to_die:
            cell.die()

        for cell in cells_to_resurrect:
            cell.resurrect()

    def __str__(self):
        list_str = []
        for cell in self.cells.values():
            list_str.append(str(cell)) #+ " - " + str(cell.neighbours))
        return "\n".join(list_str)
        
    def get_cell_neighbours(self, cell):
        row, col = cell.row, cell.col
        
        neghbouring_positions = [
            (row, col + 1),
            (row, col - 1),
            (row + 1, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row - 1, col),
            (row - 1, col + 1),
            (row -1, col - 1)
            ]

        return [
            self.cells.get(pos) for pos
            in neghbouring_positions if self.cells.get(pos)
            ]
        