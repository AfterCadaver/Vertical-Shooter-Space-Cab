__author__ = 'AFTERCADAVER:smells'

import json, sys, os
import pygame as pg
from math import sin, pi
from .. import setup,tools
from .. import constants as c

class Menu(tools.State):

    #THE STATE FOR THE OPENING SCENE
    
    def __init__(self):
        super(Menu, self).__init__()
        self.font = pg.font.Font(setup.FONTS['astron boy wonder'],35)
        self.volume = 0.4
        self.name, self.next = c.MENU, c.EMAIL1
        self.startup(0, 0)

    def draw_level(self, surface):
        surface.fill(c.b)
        
        rel_y = self.y % 800

        #THE SCROLLING BACKGROUND
        
        surface.blit(self.bgSurf, (0,rel_y - 800))
   
        if  rel_y < 800:
        
            surface.blit(self.bgSurf, (0, rel_y))

        #THE TITLE

        current_scale = self.title_scale
        scale_increase = 6

        if self.title_scale < self.title_max_scale:

            self.title_scale += scale_increase

        img = pg.transform.scale(self.title,
                                 (current_scale,current_scale))

        img_rect = img.get_rect()

        #THE SUBTITLE

        surface.blit(img,
                     ((550 - img_rect.width) / 2,235 - img_rect.height / 5))

        surface.blit(self.image,
                     (80,550))

    def startup(self, *args):

        if not os.path.isfile('save.json'):
            self.game_data = tools.create_game_data_dict()

        else:
            self.game_data = json.load(open('save.json','r'))

        #dfgdhfjfgjhgfjh

        if not self.game_data['game complete']:
            self.bgSurf = setup.GFX[self.game_data['last level']]
            self.scroll_speed = 5
            self.music_title = 'opening_music'
            self.music = setup.MUSIC['opening_music']

        else:
            self.bgSurf = setup.GFX['level1']
            self.scroll_speed = 5
            
        self.bgSurfRect = self.bgSurf.get_rect()

        #THE TITLE

        self.title = setup.GFX['space_cab']
        self.title_rect = self.title.get_rect()

        #THE SUBTITLE

        self.image = self.make_image()

        #STATEDICT

        self.state_dict = self.make_state_dict()
        self.state = c.MENU

        self.y = 0
        self.title_scale = 100
        self.title_max_scale = 300

        self.next = self.set_next_scene()

    def make_image(self):
        '''
        TEST FOR TEXT RENDER
        '''
        this = self.font.render('An Underdog\'s Story',True,c.g)

        return this
    
    def make_viewport(self, image):
        pass
    
    def make_state_dict(self):

        '''
        MAKE DICTIONARY OF STATES IN LEVEL
        '''
        state_dict ={c.TRANSITION: self.transition,
                     c.MENU:self.normal_update
                    }

        return state_dict

    def transition(self):
        pass
    
    def update(self,surface, *args):
        
        '''
        update
        '''

        update_level = self.state_dict[self.state]
        update_level()
        self.draw_level(surface)
        self.y += self.scroll_speed
        
    def get_event(self,event):
        if event.type == pg.KEYUP:
            self.done = True

        if event.type == pg.MOUSEMOTION:
            print('YES')

    def set_next_scene(self):
        '''
        CHECK FOR SAVED GAME.IF NOT START AT BEGINNING
        '''
        if not os.path.isfile('save.json'):
            next_scene = c.MESSAGE
        else:
            next_scene = c.LOADGAME

        return next_scene

    def normal_update(self):
        pass

class loadGame(tools.State):
    def __init__(self):
        super(loadGame, self).__init__()
        self.arrow = None
        self.state = c.NORMAL
        self.allow_input = True
        self.background = setup.GFX['level1']
        self.y, self.scroll_speed = 1, 5

    def make_state_dict(self):
        
        #MAKE DICTIONARY OF STATES IN LEVEL
        
        state_dict = {c.NORMAL:self.normal_update,
                      c.TRANSITION:self.transition
                      }
        return state_dict

    def transition(self):
        self.done = True

    def startup(self, current_time, game_data):

        self.game_data = json.load(open('save.json','r'))

        self.state_dict = self.make_state_dict()

        #self.background = setup.GFX[']

        self.lrg_font = pg.font.Font(setup.FONTS['astron boy wonder'],
                                     75)

        self.med_font = pg.font.Font(setup.FONTS['astron boy wonder'],
                                     35)

        self.sml_font = pg.font.Font(setup.FONTS['astron boy wonder'],
                                     28)
        self.set_next_scene()

        self.image = self.lrg_font.render('LOAD GAMES',
                                          True,
                                          c.w)
        
        self.load_game_1 = self.med_font.render('SAVE 1:',
                                                True,
                                                c.w)
        
        self.game1_sub = self.sml_font.render(self.game_data['last level'],
                                               True,
                                               c.w)
        
        self.load_game_2 = self.med_font.render('SAVE 2:',
                                                True,
                                                c.f)
        
        self.load_game_3 = self.med_font.render('SAVE 3:',
                                                True,
                                                c.c)

    def get_event(self,event):
        pass

    def draw_level(self,surface):
        
        #blit background to scene
        
        self.y += self.scroll_speed

        rel_y = self.y % 800

        surface.blit(self.background,
                     (0, rel_y - 800))

        if rel_y <= 800:

            surface.blit(self.background,
                         (0, rel_y))
            
        surface.blit(self.image,
                     (0, 0))

        surface.blit(self.load_game_1,
                     (100, 200))

        surface.blit(self.game1_sub,
                     (130,250))
            
        surface.blit(self.load_game_2,
                     (100, 400))
        
        surface.blit(self.load_game_3,
                     (100, 600))

    def set_next_scene(self):

        mouse_over = None

        if mouse_over:
            pass

    def update(self,surface,keys,current_time):
        update_level = self.state_dict[self.state]
        update_level(keys)
        
        self.draw_level(surface)

    def normal_update(self,keys):
        
        if keys[pg.K_SPACE]:
                self.next = 'menu'
                self.state = self.transition()
                

    
