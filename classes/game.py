from tkinter import Canvas


class Cell:

    def __init__(self, canvas, x, y, cell_width):
        self.is_alive = False
        self.canvas = canvas
        self.x = x
        self.y = y
        self.x1 = x + cell_width
        self.y1 = y + cell_width
        self.object_id = None

    def draw(self, alive=False):
        if self.object_id:
            self.canvas.delete(self.object_id)

        self.object_id = self.canvas.create_rectangle(
            self.x, self.y, self.x1, self.y1, fill='black' if not alive else 'white', outline='white')

    def born(self):
        self.is_alive = True
        self.draw(self.is_alive)

    def toggle_state(self):
        self.is_alive = not self.is_alive
        self.draw(self.is_alive)

    def change_state(self, alive: bool):
        self.is_alive = alive
        self.draw(self.is_alive)


class Universe:

    def __init__(self, root):
        self.cell_width = 10
        self.width = 400
        self.height = 400
        self.canvas = Canvas(root, width=self.width, height=self.height)
        self.cells_number = int(self.width / self.cell_width)
        self.cells: list[list[Cell]] = []
        self.initialize_canvas()
        self.life_inited = False
        self.canvas.bind('<Button-1>', self.cell_clicked)

    def initialize_canvas(self):
        self.create_cells()
        self.canvas.pack()

    def create_cells(self):
        cells_row = []

        for i in range(self.cells_number):

            if i > 0:
                self.cells.append(cells_row)
                cells_row = []

            for j in range(self.cells_number):
                x = i * self.cell_width
                y = j * self.cell_width

                new_cell = Cell(self.canvas, x, y, self.cell_width)
                new_cell.draw()

                cells_row.append(new_cell)

        self.cells.append(cells_row)

    def cell_clicked(self, event):
        if self.life_inited:
            return

        x_clicked = int(event.x / self.cell_width)
        y_clicked = int(event.y / self.cell_width)

        self.cells[x_clicked][y_clicked].toggle_state()

    def calculate_neighbors_range(self, coord):
        neighbor_range_inf = coord - 1 if coord - 1 > 0 else 0
        neighbor_range_sup = coord + 1 if coord + \
            1 < self.cells_number else self.cells_number - 1
        return (neighbor_range_inf, neighbor_range_sup)

    def get_alive_neighbors(self, i, j):
        x_range_inf, x_range_sup = self.calculate_neighbors_range(i)
        y_range_inf, y_range_sup = self.calculate_neighbors_range(j)

        alive_neighbors = 0
        for x in range(x_range_inf, x_range_sup + 1):
            for y in range(y_range_inf, y_range_sup + 1):
                if x == i and y == j:
                    continue

                if self.cells[x][y].is_alive:
                    alive_neighbors += 1

        return alive_neighbors

    def tick(self):
        new_states = []
        new_states_column = []
        column_number = len(self.cells)
        for i in range(column_number):
            row_number = len(self.cells[i])

            if i > 0:
                new_states.append(new_states_column)
                new_states_column = []

            for j in range(row_number):
                current_cell = self.cells[i][j]

                live = current_cell.is_alive

                alive_neighbors = self.get_alive_neighbors(i, j)

                if not live and alive_neighbors == 3:
                    live = True

                if live and alive_neighbors >= 2 and alive_neighbors <= 3:
                    live = True

                if live and (alive_neighbors > 3 or alive_neighbors <= 1):
                    live = False

                new_states_column.append(live)
        new_states.append(new_states_column)

        for i in range(len(new_states)):
            for j in range(len(new_states[i])):
                cell_lives = new_states[i][j]
                cell_lives != self.cells[i][j].is_alive and self.cells[i][j].change_state(
                    cell_lives)
