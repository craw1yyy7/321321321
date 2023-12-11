import pygame as pg

W = 800
H = 600
game_over = False 

pg.init()
screen = pg.display.set_mode((W, H))
pg.display.set_caption(">>>")


x = 0
y = 0
prav_x = W / 4 + 17
prav_y = H / 2 - 26
lev_x = W / 4 - 78
lev_y = H / 2 - 25

r = 6
COLOR_BLUE = (20, 18, 222)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = ((255,100,10))

clock = pg.time.Clock()

while not game_over:
    screen.fill(COLOR_BLACK)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == 27 or event.type == pg.QUIT:
            game_over = True
    if x > W - 200:
        x = -200
    if prav_x > W -20:
        prav_x = -20
    if lev_x > W -70:
        lev_x = -70
             
    x += 5
    lev_x += 5
    prav_x += 5
    
    pg.draw.rect(screen, COLOR_BLUE, (x + 50, 250, 300, 200,))
    pg.draw.rect(screen, COLOR_RED, (x + 100,350, 240, 30,))
    pg.draw.rect(screen, COLOR_ORANGE, (x + 100,300, 15, 15,))
    pg.draw.rect(screen, COLOR_ORANGE, (x + 300,300, 15, 15,))
    

    pg.display.update()
    clock.tick(60)