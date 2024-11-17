import pygame as pg
pg.init()

mus1 = "C:\\PP2\\lab7\\mus1.mp3"
mus2 = "C:\\PP2\\lab7\\mus2.mp3"
mus3 = "C:\\PP2\\lab7\\mus3.mp3"
screen = pg.display.set_mode((360, 360))
pg.display.set_caption("player")

musicList = [mus1, mus2, mus3]
i = 0
pg.mixer.music.load(musicList[i])
pg.mixer.music.play()

back = (0, 0, 0)

flPlay = False
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
                    
            elif event.key == pg.K_RIGHT:
                i += 1
                if i == len(musicList):
                    i = 0
                pg.mixer.music.load(musicList[i])
                pg.mixer.music.play()
                
            elif event.key == pg.K_LEFT:
                i -= 1
                if i == -1:
                    i = len(musicList)-1
                pg.mixer.music.load(musicList[i])
                pg.mixer.music.play()
    
    screen.fill(back)

pg.quit()