import pygame as pg 
import numpy as np
from pygame_objects import text, button 
from life import gol 

def play_fn(*args):
    global play_flag
    play_flag = True

def pause_fn(*args):
    global play_flag
    play_flag = False

def next_fn(*args):
    game.update()

def rset_fn(*args):
    game.reset()

def mode_fn(*args):
    global mode_flag, game, game1, game2
    mode_flag = not mode_flag
    if mode_flag:
        game = game1
    else:
        game = game2

if __name__ == '__main__':
    pg.init()
    screen_size = (1500, 800)
    size        = 10
    clr         = np.array([255, 0, 255])
    bg          = (255, 255, 0)
    block_size  = 10
    font_size   = 15
    font        = pg.font.Font(None, font_size)
    clock       = pg.time.Clock()

    screen    = pg.display.set_mode(screen_size)
    screen.fill(bg)
    pg.draw.rect(screen, (0, 255, 255), [[195, 0], [1300, 705]], 10)
    leftsurf  = pg.Surface((190, 800))
    botmsurf  = pg.Surface((1320, 95))

    game1 = gol(130, 70, 10)
    # game1.insert(game1.glider, (0, 0))
    game1.insert(game1.blinker, ( 1, 1))
    game1.insert(game1.toad,    ( 6, 1))
    game1.insert(game1.beacon,  (15, 1))
    game1.insert(game1.pulsar,  (30, 1))
    game1.insert(game1.pent_dc, (50, 1))
    game1.insert(game1.LWSS,    ( 0, 120), 270)
    game1.insert(game1.glider_gun, (0, 40))
    # game1.insert(game1.puffer_train, (40, 30))
       
    game2 = gol(130, 70, 10)
    for i in range(1000):
        game2.insert([[1]], (np.random.randint(0, 70), np.random.randint(0, 130)))
       
    play  = button((850, 750), (50, 50), (220, 220, 220), (255, 255, 0), play_fn, 'RUN')
    pause = button((800, 750), (50, 50), (220, 220, 220), (255, 255, 0), pause_fn, '||')
    nxt   = button((900, 750), (50, 50), (220, 220, 220), (255, 255, 0), next_fn,  '>>')
    mode  = button((500, 750), (200, 50), (220, 220, 220), (255, 255, 0), mode_fn, 'change mode')
    rset  = button((1150, 750), (200, 50), (220, 220, 220), (255, 255, 0), rset_fn, 'reset')

    button_list = [play, pause, nxt, mode, rset]

    crash = True
    play_flag = False
    mode_flag = True
    game = game1
    while crash:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crash = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    crash = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pg.mouse.get_pos()
                    for b in button_list:
                        if b.rect.collidepoint(pos):
                            b.call_back()


        leftsurf.fill((255, 255, 0))
        botmsurf.fill((0, 255, 255))
        if play_flag:
            game.update()
        game.draw(screen, (195, 5))
        screen.blit(leftsurf, (0, 0))
        screen.blit(botmsurf, (190, 710))
        for b in button_list:
            b.draw(screen)

        t = text("Conway's", (100, 100), clr=[255, 0, 255], font_size=35, mid=True)
        t.draw(screen)         
        t = text("game", (100, 150), clr=[255, 0, 255], font_size=35, mid=True)
        t.draw(screen)         
        t = text("of", (100, 200), clr=[255, 0, 255], font_size=35, mid=True)
        t.draw(screen)         
        t = text("life", (100, 250), clr=[255, 0, 255], font_size=35, mid=True)
        t.draw(screen)         

        t = text("generation: "  + str(game.gen), (100, 350), clr=[0, 0, 0], font_size=15, mid=True)
        t.draw(screen)         
        t = text("alive: "  + str(game.alive), (100, 380), clr=[0, 0, 0], font_size=15, mid=True)
        t.draw(screen) 
        t = text("current mode: ", (100, 730), clr=[0, 0, 0], font_size=15, mid=True)
        t.draw(screen)         
        t = text('custom' if mode_flag else 'random' , (100, 750), clr=[0, 0, 0], font_size=15, mid=True)
        t.draw(screen)         
        cur_fps = font.render(str(int(clock.get_fps())), False, (255, 0, 0))
        screen.blit(cur_fps, (10, 10))
        pg.display.update()
        clock.tick(144)
