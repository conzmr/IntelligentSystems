import heapq
import time
import turtle

SECONDS_OF_DELAY = 1
GRID_SIZE = 5
OBSTACLES = ((0, 5), (1, 0), (1, 1), (1, 5), (2, 3),
     (3, 1), (3, 2), (3, 5), (4, 1), (4, 4), (5, 1))
BACKGROUND_COLOR = "black"
OBSTACLES_COLOR = "white"
PATH_COLOR = "red"
TEXT_COLOR = "white"
START_POSITION = (0,0)
GOAL_POSITION = (5,5)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

    def set_color(self, color):
        self.color(color)

    def paint(self, list, color):
        self.color(color)
        for x in range (len(list)):
            screen_x = -288 + (list[x][0] * 24)
            screen_y = 288 - (list[x][1] * 24)
            self.goto(screen_x, screen_y)
            self.stamp()

    def set_tile_h(self, list, text_color, bg_color):
        for x in range (len(list)):
            screen_x = -288 + (list[x][0] * 24)
            screen_y = 288 - (list[x][1] * 24)
            self.color(bg_color)
            self.goto(screen_x, screen_y)
            self.stamp()
            self.color(text_color)
            self.write(list[x][2], False, align="center")



class Tile(object):
    def __init__(self, x, y, obstacle):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        self.obstacle = obstacle
        self.parent = None

class MazeSolver(object):
    def __init__(self):
        self.open_set = []
        self.close_set = set()
        self.tiles = []
        self.maze_height = None
        self.maze_width = None
        heapq.heapify(self.open_set)

    def set_grid(self, width, height, walls, start, end):
        self.maze_height = height
        self.maze_width = width
        for x in range(self.maze_width):
            for y in range(self.maze_height):
                if (x, y) in walls:
                    obstacle = True
                else:
                    obstacle = False
                self.tiles.append(Tile(x, y, obstacle))
        self.start = self.get_tile(*start)
        self.end = self.get_tile(*end)

    def get_tile(self, x, y):
        return self.tiles[x * self.maze_height + y]

    def set_tile(self, adj, tile):
        adj.g = tile.g + 10
        adj.h = self.get_heuristic(adj)
        adj.f = adj.h + adj.g
        adj.parent = tile

    def get_adjacent_tiles(self, tile):
        tiles = []
        if tile.x < self.maze_width-1:
            tiles.append(self.get_tile(tile.x+1, tile.y))
        if tile.y > 0:
            tiles.append(self.get_tile(tile.x, tile.y-1))
        if tile.x > 0:
            tiles.append(self.get_tile(tile.x-1, tile.y))
        if tile.y < self.maze_height-1:
            tiles.append(self.get_tile(tile.x, tile.y+1))
        return tiles

    def get_maze_tiles(self):
        tiles = []
        for tile in self.tiles:
            if not tile.obstacle:
                tiles.append((tile.x, tile.y, tile.h))
        return tiles

    def get_path(self):
        tile = self.end
        path = [(tile.x, tile.y)]
        while tile.parent is not self.start:
            tile = tile.parent
            path.append((tile.x, tile.y))

        path.append((self.start.x, self.start.y))
        path.reverse()
        return path

    def get_heuristic(self, tile):
        return (abs(tile.x - self.end.x) + abs(tile.y - self.end.y)) * 10

    def get_solution(self):
        heapq.heappush(self.open_set, (self.start.f, self.start))
        while len(self.open_set):
            print(self.get_maze_tiles())
            h_pen = Pen()
            h_pen.set_tile_h(self.get_maze_tiles(), TEXT_COLOR, BACKGROUND_COLOR)
            f, tile = heapq.heappop(self.open_set)
            self.close_set.add(tile)
            if tile is self.end:
                return self.get_path()
            adj_tiles = self.get_adjacent_tiles(tile)
            for adj_tile in adj_tiles:
                if not adj_tile.obstacle and adj_tile not in self.close_set:
                    if (adj_tile.f, adj_tile) in self.open_set:
                        if adj_tile.g > tile.g + 10:
                            self.set_tile(adj_tile, tile)
                    else:
                        self.set_tile(adj_tile, tile)
                        heapq.heappush(self.open_set, (adj_tile.f, adj_tile))
            time.sleep(SECONDS_OF_DELAY)

if __name__ == '__main__':
    wn = turtle.Screen()
    wn.title("A* Maze")
    wn.bgcolor(BACKGROUND_COLOR)
    wn.setup(700,700)
    pen = Pen()
    pen.paint(OBSTACLES, OBSTACLES_COLOR)
    maze_solver = MazeSolver()
    maze_solver.set_grid(6, 6, OBSTACLES, (0, 0), (5, 4))
    path = maze_solver.get_solution()
    pen.paint(path, PATH_COLOR)
    print(path)

    while True:
        pass
