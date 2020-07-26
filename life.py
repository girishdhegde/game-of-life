import pygame as pg 
import numpy as np 

class gol:

    #################################################################################

    # Oscillators
    blinker = [[1, 1, 1]]

    toad    = [[0, 0, 0, 0],
               [0, 1, 1, 1],
               [1, 1, 1, 0],
               [0, 0, 0, 0]]

    beacon  = [[1, 1, 0, 0],
               [1, 1, 0, 0],
               [0, 0, 1, 1],
               [0, 0, 1, 1]]

    pulsar  = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
               [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
               [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
               [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
               [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    pent_dc = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],               
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


    # Spaceships
    glider = [[0, 0, 1],
              [1, 0, 1],
              [0, 1, 1]]

    LWSS   = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 1, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]


    # Guns
    glider_gun   = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    puffer_train = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #################################################################################

    # rules
    conway_gol = 'B3/S26'
    replicator = 'B1357/S1357'
    high_life  = 'B36/S23'

    #################################################################################

    deadclr = ( 30,  30,  30)
    lineclr = ( 40,  40,  40)
    liveclr = (255,   0,   0)

    def __init__(self, w=150, h=80, cell_size=10):
        self.width = w
        self.hgt   = h
        self.size  = cell_size
        self.world = np.zeros((w + 2, h + 2), np.uint8)
        self.surf  = pg.Surface((w * cell_size, h * cell_size))
        self.sarr  = np.ones((w * cell_size, h * cell_size, 3), np.uint8) * self.deadclr
        self.B     = [3]
        self.S     = [2, 3]
        self.gen   = 0
        self.alive = 0
        self.rule()

        for i in range(cell_size, w * cell_size, cell_size):
            self.sarr[i][:] = self.lineclr

        for j in range(cell_size, h * cell_size, cell_size):
            for i in range(w * cell_size):
                self.sarr[i][j] = self.lineclr


    def rule(self, bs_string='B3/S23'):
        bs     = bs_string.split('/')
        self.B = list(map(int, bs[0][1:]))
        self.S = list(map(lambda x: int(x) + 1, bs[1][1:]))
        

    def update(self):
        self.next  = self.world.copy()
        self.alive = 0
        self.gen  += 1
        for col in range(1, self.width + 1):
            for row in range(1, self.hgt + 1):
                neighbours = np.sum(self.world[col - 1: col + 2, row - 1: row + 2])           
                # birth
                if not self.world[col, row]:
                    if neighbours in self.B:
                        self.next[col, row] = 1
                        self.draw_cell(row - 1, col - 1, 1)
                # death
                if self.world[col, row]:
                    self.alive += 1
                    if neighbours not in self.S:
                        self.next[col, row] = 0
                        self.draw_cell(row - 1, col - 1, 0)
        self.world = self.next

    def insert(self, obj, topleft=(0, 0), rotate=0):
        obj  = np.array(obj)
        obj  = np.rot90(obj, rotate//90)
        w, h = obj.shape
   
        for row in range(w):
            for col in range(h):
                if obj[row, col] != -1:
                    ROW = row + topleft[0] 
                    COL = col + topleft[1] 
                    self.world[COL + 1, ROW + 1] = obj[row, col]
                    self.draw_cell(ROW, COL, obj[row, col])
        self.reset_world = self.world.copy()
        self.reset_sarr  = self.sarr.copy()

    def draw(self, screen, pos=(0, 0)):
        pg.surfarray.blit_array(self.surf, self.sarr)
        screen.blit(self.surf, pos)

    def draw_cell(self, i=0, j=0, state=1):
        srtx = i * self.size
        srty = j * self.size
        if state:
            self.sarr[srty + 1: srty + self.size, srtx + 1: srtx + self.size] = self.liveclr
        else:
            self.sarr[srty + 1: srty + self.size, srtx + 1: srtx + self.size] = self.deadclr

    def reset(self):
        self.world = self.reset_world.copy()
        self.sarr  = self.reset_sarr.copy()
        self.gen   = 0
        self.alive = 0

if __name__ == '__main__':


    pg.init()


    screen_size = (1500, 800)
    size        = 10
    clr         = np.array([255, 0, 255])
    bg          = (255, 255, 255)
    block_size  = 10
    font_size   = 15
    font        = pg.font.Font(None, font_size)
    clock       = pg.time.Clock()

    # surf = pg.Surface(screen_size)
    screen    = pg.display.set_mode(screen_size)

    game = gol(150, 79, 10)
    # game.insert(game.burst, (40, 75))
    game.insert(game.glider, (0, 0))
    game.insert(game.blinker, (70, 70))
    # game.rule('B1357/S1357')
    # game.rule('B36/S23')
    # for i in range(200):
    for i in range(50):
        game.insert(game.glider, np.random.randint(0, 70, 2))
       

    crash = True
    while crash:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crash = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    crash = False
        game.update()
        screen.fill(bg)
        game.draw(screen)
        # cur_fps = font.render(str(int(clock.get_fps())), False, (255, 0, 0))
        # screen.blit(cur_fps, (10, 10))
        pg.display.update()
        clock.tick(144)
