import pygame
import math
from queue import PriorityQueue

# 1- we set how wide the square is going to be
WIDTH = 800

WIN = pygame.display.set_mode((WIDTH, WIDTH))
# 2- set a caption for the display
pygame.display.set_caption("A* Path finding Algorithm")

# 3- Find colors code/using them for path, squares, etc
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)



# capital letters as constants
# 4- define class call spot/or Node //to build the main visualization tool/before implementing the algorythm
# the algorithm will depend of what the tool look like
# 5- How to keep truck of the node that are in the grid
# they will be 50/50 grid we can change them if we want
# in the grid we will have spots, and cube ect
# the spot will have value, and keep track of rows, columns etc
# keep truck of the different node
class Spot:
    def __init__(self, row, col, width, total_rows ):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # 6- Create a PoS method which will return rows and colusmn
    def get_pos(self):
        return self.row, self.col
    #7- create a closed method where we check if the node was visited already
    # what makes a spot closed(we are not looking at it anymore/what makes it red
    # we are going to have bunch method which tell us the state of the spot
    # and update the state of the spot as well
    # if the color is red, we already visited, if it white we havent visited it, if its black
    # its a barrier to avoid, the algorythm can't use that as a node to visit
    # Orange is the start node
    #purple is the path


    def is_closed(self):
        return self.color == RED

    def is_opened(self):
        return self.color == GREEN
    def is_barrrier(self):
        return self.color == BLACK
    def is_start(self):
        return self.color == ORANGE
    def is_end(self):
        return self.color == TURQUOISE
    def reset(self):
        return self.color== WHITE

    #9- make
    def make_closed(self):
        self.color== WHITE
    def make_opened(self):
        self.color==GREEN
    def make_barrier(self):
        self.color==BLACK
    def make_start(self):
        self.color==ORANGE
    def make_end(self):
        self.color==TURQUOISE
    def make_reset(self):
        self.color == WHITE

    def make_path(self):
        self.color== PURPLE

    def make_start(self):
        self.color == ORANGE

    #10- we gonna draw on the widow

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))


    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False
    # 11- meaning less than this is what happen when we compare two spots(class Spot  and other spot) together
    # the other spots are greater than the actual spot

    #12- We define the heuristic function for algorythm
    # the h function contains point 1 and point 2
    # the expectation is to look lie x and y row and column
    # we need to figue out the distance betwn p1 and p2 and return it
    # the way we do it is by doing manathan distance or taxi cab distaance
    # abs() will remove the negative example abs(-8) = 8

def h(p1, p2):
    x1,y1 = p1
    x2, y2 = p2
    return abs(x1 - x2)+ abs(y1-y2)

    # 13- need a data stracture that can hold all the spots, to use them, traverse the grid
    # Its gonna be a list that can hold all the spots
    # how many we want in the grid
    # width is the widht of the enire grid
    # rows is how many rows we have by doing an integer division
    # the gap between all the rows
    # i = rows, j is the column

def make_grid(rows, width):
    grid = []
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap,rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):

        pygame.draw.line(win, GREY, (0, i * gap ), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
            # 14- for every row we draw a horizontal line for one of the rows
            # then we pass them on the win(window) we pass the color and and we set two xy positions from
            # where the line will start snd where its gonna end()()
            # the start of  the line we want it to be at x =0, the the y = i*gap
            # and thrn x = width, and y = i *gap

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
        gap = width//rows
        y,x = pos
        row = y//gap
        col = x//gap
        return row, col

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:# left
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot  != end :
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()


main(WIN, WIDTH)


















































































































