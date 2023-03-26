from tkinter import Canvas


class Cell:

    def __init__(self, canvas, x, y, cell_width):
        self.is_alive = False
        self.canvas = canvas
        self.x = x
        self.y = y
        self.x1 = x + cell_width
        self.y1 = y + cell_width

    def draw(self, alive=False):
        print(self.x, self.y , self.x1, self.y1)
        self.canvas.create_rectangle(
            self.x, self.y, self.x1, self.y1, fill='black' if not alive else 'white', outline='white')

    def born(self):
        self.is_alive = True
        self.draw(self.is_alive)


class Universe:

    def __init__(self, root):
        self.cell_width = 10
        self.width = 400
        self.height = 400
        self.canvas = Canvas(root, width=self.width, height=self.height)
        self.cells_number = int(self.width / self.cell_width)
        self.cells = []
        self.initialize_canvas()
        self.canvas.bind('<Button-1>', self.cell_clicked)

    def initialize_canvas(self):
        self.create_cells()
        self.canvas.pack()

    def create_cells(self):
        for i in range(self.cells_number):
            for j in range(self.cells_number):
                x = i * self.cell_width
                y = j * self.cell_width

                new_cell = Cell(self.canvas, x, y, self.cell_width)
                new_cell.draw()

                self.cells.append(new_cell)

    def change_cell_state(self, x_clicked: int, y_clicked: int):
        x = x_clicked * self.cell_width
        y = y_clicked * self.cell_width

        x1 = x + self.cell_width
        y1 = y + self.cell_width

        self.canvas.create_rectangle(x, y, x1, y1, fill='white')

    def cell_clicked(self, event):
        print('Clcici', event.x, event.y)

        x_clicked = int(event.x / self.cell_width)
        y_clicked = int(event.y / self.cell_width)

        print(x_clicked, y_clicked)

        self.change_cell_state(x_clicked, y_clicked)
