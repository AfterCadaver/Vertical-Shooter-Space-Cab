import pygame  as pg
from os import path
import random
from math import pi, sin
from behaviors import *

# initialize game engine

pg.init()

# set screen size and caption

pg.display.set_caption('Space Cab')

icon = pg.image.load(path.join(img_folder,'ship.png'))

pg.Surface.set_colorkey(icon,b)

pg.display.set_icon(icon)

Clock = pg.time.Clock()

ds = pg.display.set_mode(size)

# define fonts

done = False

font = pg.font.SysFont(None, 30)

impact = pg.font.match_font('impact')

smallfont = pg.font.SysFont(None, 15)

font_name = pg.font.match_font('times')

background = pg.image.load(path.join(img_folder,'bg_space.png')).convert_alpha()

pg.mixer.music.load(path.join(music_folder, "opening_music.ogg"))

class ship(pg.sprite.Sprite):
    #The Player Class
    def __init__(self):
        pg.sprite.Sprite.__init__(self, level_objects)
        self.image = pg.image.load(path.join(img_folder, 'ship.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (200, 700)
        self.speedx = 0
        self.speedy = 0
        self.shield = 100
        self.playing = True
        self.reg_limit = 100

    def controls(self):

        keystate = pg.key.get_pressed()

        if keystate[pg.K_LEFT]:
            self.speedx = -10

        if keystate[pg.K_RIGHT]:
            self.speedx = 10

        if keystate[pg.K_UP]:
            self.speedy  = -10

        if keystate[pg.K_DOWN]:
            self.speedy = 10

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > size[0]:
            self.rect.right = size [0]

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > size [1]:
            self.rect.bottom = size [1]

        #if self.rect.   

        if self.shield < self.reg_limit:
            self.shield += 0.2

        if self.shield < 50:

            self.reg_limit = 50

    def shoot(self):

        #fire projectiles

        bullet = blasts(self.rect.centerx, self.rect.top + 30)

        bullets.add(bullet)

        self.shield -= 5

    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.controls()

class blasts(pg.sprite.Sprite):
    """projectiles for the space cab"""
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self, level_objects, bullets)
        self.image        =  pg.Surface((6, 72))
        self.fill         = self.image.fill(w)
        self.rect         = self.image.get_rect()
        self.rect.bottom  = y
        self.rect.centerx = x
        self.speedy       = -40

    def update(self):
        self.rect.bottom += self.speedy

        if self.rect.bottom <= 0:
            self.kill()

class brakar_3(enemy):
    """ Class for first enemy, brakar_1"""
    def __init__(self, trait):
        enemy.__init__(self)
        pg.sprite.Sprite.__init__(self, level_objects)
        self.image    = pg.image.load(path.join(img_folder,'en_brakar_3.png')).convert_alpha()
        self.rect     = self.image.get_rect()
        self.rect.x   = 0
        self.rect.y   = 110
        self.shield   = 25
        self.counting = 0

    def update(self):

        after_finished ='AI: old friend detected up ahead'

        if shield <= 0:

            defeat =  textBox(after_finished)

            self.kill()

        self.sine()

        if not self.counting:
            
            bullet = attack(self.rect.centerx, self.rect.centery)

            self.counting = 15

        if self.counting:

            self.counting -= 1

class Brakar(enemy):
    """docstring for Brakar"""
    def __init__(self):
        enemy.__init__(self)
        pg.sprite.Sprite.__init__(self, level_objects)
        self.image = pg.image.load(path.join(img_folder,'b1_Brakar.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 275
        self.rect.y = 400
        self.counting = 40
        self.shield = 0
    
    def movement(self):
        
        self.number += 1

        #MOVE AT DIFFERENT RATES TO APPROXIMATE INFINITY SYMBOL

        self.rect.centerx = 275 * sin(self.number * 0.5 * pi / 60) + 275
        self.rect.centery = 100 * sin(self.number * 0.5 * pi / 30 ) + 200

    def update(self):
   
        self.movement()

        if self.shield <= 0:

            last_words = textBox('Wait, wait, I wasn\'t ready!', 2, r) 

            self.kill()

        if not self.counting:

        # on count of 4 fire two simultaneous shots from arms

            shot1 = attack(self.rect.centerx + 240, self.rect.bottom - 20)

            shot2 = attack(self.rect.centerx - 250, self.rect.bottom - 20)

            self.counting = 4
        
        if self.counting:

            self.counting -= 1 

class attack(pg.sprite.Sprite):
    """basic projectile for brakars"""
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self, level_objects)
        self.image = pg.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.fill = self.image.fill((0,0,0,0))
        self.rect.top = y
        self.rect.x = x
        self.speedy = 10
        self.rate = 0
        
    def update(self):

            self.rate += 1

            pg.draw.circle(self.image, (255, 0, 0), (10, 10), 10, 6)

            self.rect.centery += self.speedy

            if self.rect.top > 800:
                self.kill() 

class textBox(pg.sprite.Sprite):
    """docstring for textBox"""
    def __init__(self, text, speed = 5, color = (0, 0, 0)):
        pg.sprite.Sprite.__init__(self, gui)
        self.image = pg.image.load(path.join(img_folder, 'obj_textbox.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = (size[0] - self.rect.width) / 2
        self.rect.y = size[1] - self.rect.height       
        self.font = pg.font.SysFont("courier new bold", 20)
        self.count = speed
        self.counting = 0
        self.pos = 120
        self.string = text
        self.list = list(self.string)
        self.speaker = color

    def update(self):

        keystate = pg.key.get_pressed()

        if not self.counting and self.list:
            
            letter = self.list.pop(0)
            
            s =  self.font.render(letter, 10, (self.speaker))

            self.image.blit(s,(self.pos,40))

            self.pos += 10

            self.counting = self.count

        if self.counting:

            self.counting -= 1

        if not self.list and keystate[pg.K_z]:

            self.image.set_colorkey(self.speaker)

def email_screen():

    """
    caps_log = '''(captain\'s log) First day on the job, things 
are great.I just hope that nobody finds out 
my name, ****** **** '''

    news_section = '''(NEWS)"Recently a vet has been trying to wage war on gravity.'
He\'s shot missiles.Unfortunately it backfired literally.'
The vet is retaliatng by firing at gravity.'
He shot his foot.It did\'nt work.'
in other news if you go to the'
great prince cuttle it will now finally take 50% '
for your life FOR FREE!''' 
   
    AI = '(AI) jump gate coordinates: .1926.3176 20% DANGER...',"""

    waiting = True

    y = 0

    while waiting:
        
        ds.fill(b)
        
        if y < 400:
            
            y += 1

        for event in pg.event.get():

            if event.type == pg.KEYUP and event.key == pg.K_SPACE:

                waiting = False
                
            if event.type == pg.QUIT:
                pg.quit()

        level_objects.update()

        level_objects.draw(ds)

        screenTransition(y)

        pg.display.flip()

    pg.mixer.music.load(path.join(music_folder, "will of the whistles.ogg"))

    pg.mixer.music.play(-1)

y = 0

game_over = True

#MAIN LOOP

rate = 10

levelspeed = 1

reading = False

playing = False

while done == False:

    # Events

    Clock.tick(FPS)

    if game_over:

        pg.mixer.music.play(-1)

        level_objects = pg.sprite.Group()

        gui = pg.sprite.Group()

        bullets = pg.sprite.Group()

        enemies = pg.sprite.Group()
        
        show_go_screen()

        email_screen()

        player = ship()

        score = 0

        counter = 0 

        lose = False

        level_beat = False

        game_over = False
    
    if lose:
        
        GameOver()

        done = True

    for event in pg.event.get():

        if event.type == pg.QUIT:
            done = True

        if event.type == pg.KEYUP and event.key == pg.K_m:
            
            if player.playing:

                pg.mixer.music.pause()
                player.playing = not player.playing

            else:

                pg.mixer.music.unpause()
                player.playing = not player.playing

        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                player.shoot()

#background details

    scrollingScreen(background, y)
        
    y += rate

#level

    counter += levelspeed 
    
    if counter ==  300:

        en_formation_1(level_objects, 5,  20, 3, 1,  140)

    if counter ==  600:
        
        en_formation_2(level_objects, 2, 420, 3, 1,   60, trait = 2)

    if counter ==  780:
        
        en_formation_2(level_objects, 2, 100, 6, 0,   30, trait = 1)

    if counter ==  960:
        
        en_formation_2(level_objects, 3, 200, 2,  2,  50, trait = 0)
        
    if counter == 1200:
        
        en_formation_2(level_objects, 6,  80, 4,  0,  50)
        
    if counter == 1380:
        
        en_formation_3(level_objects, 8,   5, 2, 40,   2)

    if counter == 1740:
        
        en_formation_2(level_objects, 2,  50, 5,  0, 250)
        
        en_formation_2(level_objects, 2, 450, 4,  0,   0, 1)
    
    if counter == 2100:
        
        en_formation_2(level_objects, 3, 110, 5,  2, 150)

    if counter == 2400:
        
        boss_1 = brakar_3(1)

    if counter == 3000:

        en_formation_2(level_objects, 3, 100, 5, 2, 200)

    if counter == 3100:

        pg.mixer.music.load(path.join(music_folder, "gloomy monday.ogg"))

        pg.mixer.music.play(-1)

    if counter == 3590:
        
        line_2 = 'Hey, remember me?...'
        line_3 =" Sorry, I don't want any trouble..."
        line_4 = 'You should\'nt piss off the boss! Ha Ha!'
        line_5 ="Is that Brakar ? ... Oh no..."

    if counter == 3600:
        
        en_formation_2(level_objects, 5, 110, 1, 0, 50, 2)

        boss = Brakar()

        bBattle = True

    if counter == 4200:
        
        en_formation_2(level_objects, 5, 120, 7, 0, 80)

    if counter == 4380:
        
        en_formation_2(level_objects, 4, 120, 6, 1, 90, 2)

    if counter == 4500:
        
        en_formation_2(level_objects, 2, 100, 4, 1, 100)
        
        en_formation_2(level_objects, 1, 100,  6, 0, 240)

    if counter == 4740:
        
        en_formation_1(level_objects, 5, 6, 5, 0, 90, 2)

    if counter == 4920:
        
        en_formation_1(level_objects,8, 7, 5, 1, 70)

    if counter == 5100:
        
        pass

    if counter == 5400:
        
        pass

    if counter == 6000:
        level_beat = True

    if level_beat == True:
        pass


#update

    level_objects.update()

    gui.update()

#check for blast collisions

#draw

    #display the score

    level_objects.draw(ds)

    gui.draw(ds)

    message_to_screen(ds, str(score), g, 50, 40, 40)

    message_to_screen(ds, str(round(counter / 60)), B, 100,90, 40)

    '''if bBattle:

        draw_health(ds, 30, 20, boss.shield)'''

    draw_health(ds, 510,20, player.shield)    

    pg.display.flip()

pg.quit()
