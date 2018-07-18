import pygame as pg
import random
from math import pi, sin, sqrt
from os import path

#seting up the asset folders

game_folder = path.dirname(__file__)

snd_folder = path.join(game_folder, "music")

img_folder = path.join(game_folder, "assets")

music_folder = path.join(game_folder, "music")

# colors

w = (255,255,255)
b = (  0,  0,  0)
r = (255,  0,  0)
g = (  0,180,  0)
B = (  0,  0,180)
y = (255,255,  0)
G = (177,177,177)
f = (255, 0, 255)

#frame rate

FPS = 60

Clock = pg.time.Clock()

Clock.tick(FPS)

#setting up the display

size = [550, 800]

ds = pg.display.set_mode(size)

class enemy(pg.sprite.Sprite):
    """generic enemy class"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.range = 0
        self.speedx = 0
        self.speedy = 0
        self.num = 1
        self.number = 0
        self.offset = 0
        self.range = 275
        self.rate = 60

    def sine(self):

        self.rect.y += self.speedy 

        self.number += self.num
        self.rect.centerx = self.range * sin(self.number * 0.5 * pi / self.rate) + self.range + self.offset

    def charging(self):

        if self.rect.y >= 400 and self.reverse is False:
            self.reverse = True
            self.speedy = -self.speedy
    
    def basicMovement(self):

        self.rect.y += self.speedy
        self.rect.x += self.speedx

    def turret():
        pass

    def nMovement():
        pass

    def update(self):
        
        if self.rect.top >= 800:

            self.kill()

        if not self.trait:
            
            self.basicMovement()

        if self.trait is 1:

            self.sine()

        if self.trait is 2:

            self.basicMovement()

            if self.rect.y >= 400:
                self.speedy = -self.speedy
                self.trait = 3

        if self.trait is 3:

            self.basicMovement()

            self.acceleration += 0.6

            if self.rect.y <= 100:
               self.speedy = self.acceleration
   
class brakar_1(enemy):
    """ Class for first enemy, brakar_1"""
    def __init__(self, trait):
        enemy.__init__(self)
        self.image = pg.image.load(path.join(img_folder, 'en_brakar_1.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = -200
        self.rect.centerx = 275
        self.speedy = 0
        self.speedx = 0
        self.shield = 1
        self.trait = trait
        self.rate = 40
        self.acceleration = 0
        
class brakar_2(enemy):
    """ Class for first enemy, brakar_2"""
    def __init__(self, trait):
        enemy.__init__(self)
        self.image = pg.image.load(path.join(img_folder, 'en_brakar_2.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = -200 
        self.shield = 4
        self.trait = trait
        self.acceleration = 0

def message_to_screen(display ,msg, color,x , y, size):
    #blit text onto surface

    times = pg.font.match_font('times')
    impact = pg.font.match_font('courier')
    
    font = pg.font.Font(impact, size)
    screen_text = font.render(msg, False, color)
    text_rect = screen_text.get_rect()
    text_rect.midtop = (x, y)
    display.blit(screen_text, text_rect)

def draw_health(surf, x, y, pct):
    
    if pct < 0:
        pct = 0
    
    bar_width = 20
    
    bar_height = 300
    
    fill = (pct / 100) * bar_height
    
    offset =  bar_height - fill
    
    outline_rect = pg.Rect(x, y - 1, bar_width, bar_height + 1)
    
    fill_rect = pg.Rect(x, y + offset, bar_width, fill)
    
    pg.draw.rect(surf, (255,0,0, 0.5), fill_rect)
    
    pg.draw.rect(surf, w, outline_rect, 2)   

def show_go_screen():    

    space = pg.image.load(path.join(img_folder, 'bg_space.png')).convert()

    background = space

    y = 0
    
    min_scale = 100
    max_scale = 300
    current_scale = min_scale
    scale_increase = 12

    waiting = True

    number = 0

    while waiting:
        Clock.tick(FPS)

        y += 5

        scrollingScreen(background , y)

        titl = pg.image.load(path.join(img_folder,'space_cab.png')).convert_alpha()
        
        title = pg.transform.scale(titl,(current_scale, current_scale))

        title_rect = title.get_rect()

        ds.blit(title, (size[0] / 2 - title_rect.width / 2, 235 - title_rect.height / 2))

        current_scale += scale_increase
        
        if current_scale >= max_scale:

            scale_increase = 0

        message_to_screen(ds,
                     '-START GAME-',
                     f,
                     280,
                     550,
                     40)

        message_to_screen(ds,
                    '(C) all rights reserved.circa 1999. TearWear ltd.',
                     w,
                     270,
                     760,
                     18)

        pg.display.update()

        for event in pg.event.get():

            if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                waiting = False

            if event.type == pg.QUIT:
                pg.quit()

def screenTransition(y):

    y_pos = 0

    door =  pg.image.load(path.join(img_folder, "obj_doors.png"))
    inv_door = pg.transform.flip(door,False,True)
            
    ds.blit(door, (0,-400 + y_pos))
    ds.blit(inv_door, (0, 800 - y_pos))

def scrollingScreen(background, y = 0):

    ds.fill(b)
    
    rel_y = y % background.get_rect().height
    
    ds.blit(background, (0, rel_y - background.get_rect().height))

    if  rel_y < 800:
        
        ds.blit(background, (0, rel_y))

def gameOver():

    for results in range(2):
        
        board = Board()

        cursor = Cursor(board) 

    waiting = False

    while not leaving:
        pass

def en_formation_1 (S_G, number, spacing, speed, compos, x_axis = 0, trait = 0):

    position = 0

    offset = 0

    for members in range (number):
        
        if compos == 1:

            br = brakar_1(trait)

        else:

            br = brakar_2(trait)

        br.rect.x = x_axis + position

        br.offset = position
        
        if members >= round(number / 2):

            br.rect.y += offset

            offset -= 40

        else:
            
            br.rect.y += offset

            offset += 40

        S_G.add(br)
    
        br.speedy = speed

        position += spacing + br.rect.width

def en_formation_2 (S_G,number, spacing, speed, compos, x_axis = 0, trait = 0):
    
    position = 0

    offset = 0

    for members in range (number):
        
        if not compos:
            
            br = brakar_1(trait)
        
        elif compos is 1:
            
            br = brakar_2(trait)

        elif compos is 2:

            if members % 2 == 0: 
                
                br = brakar_1(0)
            
            else:

                br = brakar_2(2)

        if members % 2 == 0:
            
            br.num = -br.num

        if trait is not 1:
            
            br.rect.centerx = x_axis + position

        S_G.add(br)
    
        br.speedy = speed

        position += spacing

def en_formation_3 (S_G ,number, speed, compos, x_axis = 0, trait = 0):

    position = 0

    offset = 0

    for ships in range(number):

        if not compos:

            br = brakar_1(trait)

        if compos:

            br = brakar_2(trait)
        
        br.rect.y -= position

        if ships % 2 == 0:
            
            br.rect.x = 0 + x_axis

        if ships % 2 == 1:
            
            br.rect.x = size[0] - br.rect.width - x_axis

        br.speedy += speed

        position += 40

        S_G.add(br)