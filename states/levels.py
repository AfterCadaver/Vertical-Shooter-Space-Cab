__author__ = 'AFTERCADAVER: single since forever'

import pygame as pg
import collections as collect
import json, os
from .. import setup, tools, enemies, player
from .. import constants as c


class levelState(tools.State):
    def __init__(self, name):
        super(levelState, self).__init__()
        self.name = name
        self.music_title, self.previous_music= None, None
        self.done = False
        self.volume = None
        self.y = 0
    
    def startup(self, current_time, game_data):
        
        #CALL WHEN STATE IS FLIPPED TO

        self.game_data, self.current_time = game_data, current_time

        self.state,self.state_dict = 'NORMAL',self.make_state_dict()
        
        self.music, self.volume = self.set_music(),self.game_data['volume']
        
        self.background ,self.scroll_speed = self.make_background()

        #CREATE WAVES FROM JSON FILE DATA

        self.waves = self.json_reader(self.make_waves())

        self.sprites = pg.sprite.Group()

        self.player = player.ship(self.sprites)

        self.CurWave = Wave(self.sprites,
                            self.waves)

        #FOR THE TRANSITIONS

        self.transition_alpha = 255

    def draw_level(self, surface):
        
        #BLIT IMAGES TO SCREEN

        #THE SCROLLING SCREEN

        self.y += self.scroll_speed

        rel_y = self.y % 800

        surface.blit(self.background,(0, rel_y - 800))

        if rel_y <= 800:

            surface.blit(self.background, (0, rel_y))

    def make_state_dict(self):
        
        #MAKE LEVEL STATES
        
        state_dict = {'NORMAL': self.normal,
                      'PAUSE':self.pause,
                      'DIALOGUE':self.dialogue, 
                      'TRANSITION':self.transit,
                      }
 
        return state_dict
    
    def make_background(self):

        #revisit this portion!!!

        GFX_dict= {c.LEVEL1: 5,
                   c.LEVEL2: 6,
                   c.LEVEL3: 2,
                   c.LEVEL4: 6,
                   c.LEVEL5: 15,
                   c.LEVEL6: 20
                    }

        if self.name in GFX_dict:

            background = self.name

            scroll_speed = GFX_dict[self.name]

            return setup.GFX[background], scroll_speed


    def set_music(self):
        
        #SET MUSIC
        
        music_dict ={c.LEVEL1:'got your tail',
                     c.LEVEL2:'shot in the dark',
                     c.LEVEL3:'chamber danger',
                     c.LEVEL4:'The Interesting Theme',
                     c.LEVEL5:'yum yum in his tum',
                     c.LEVEL6:'yum yum in his tum'}

        if self.name in music_dict:
            music = music_dict[self.name]
            self.music_title = music
            return setup.MUSIC[music]

        else:
            return None

    def update(self, surface, keys, current_time):
        
        #UPDATE STATE
        
        state_function = self.state_dict[self.state]
        state_function(surface, keys, current_time)

    def get_event(self,event):

        #QUICKLY ACCESS GAME LEVELS AND CHANGE LAST LEVEL VALUE IN GAME DATA

        if event.type is pg.KEYUP and event.key in [pg.K_1,
                                                    pg.K_2,
                                                    pg.K_3,
                                                    pg.K_4,
                                                    pg.K_5,
                                                    pg.K_6
                                                   ]:

            if os.path.isfile('save.json'):
                #IF SAVE FILE IS IN GAME FOLDER OVERWRITE JSON DATA OR
                json.dump(self.game_data,
                          open('save.json','w'),
                          indent=7,sort_keys=True)
            else:
                #CREATE FILE AND WRITE TO IT THE JSON DATA
                json.dump(self.game_data,
                          open('save.json','x'),
                          indent=7,sort_keys=True)
                
            self.done = True
            
            
        if event.type is pg.KEYUP and event.key is pg.K_1:
            self.next = c.LEVEL1
            self.game_data['last level'] = c.LEVEL1

        if event.type is pg.KEYUP and event.key is pg.K_2:
            self.next = c.LEVEL2
            self.game_data['last level'] = c.LEVEL2

        if event.type is pg.KEYUP and event.key is pg.K_3:
            self.next = c.LEVEL3
            self.game_data['last level'] = c.LEVEL3

        if event.type is pg.KEYUP and event.key is pg.K_4:
            self.next = c.LEVEL4
            self.game_data['last level'] = c.LEVEL4

        if event.type is pg.KEYUP and event.key is pg.K_5:
            self.next = c.LEVEL5
            self.game_data['last level'] = c.LEVEL5

        if event.type is pg.KEYUP and event.key is pg.K_6:
            self.next = c.LEVEL6
            self.game_data['last level'] = c.LEVEL6

        if event.type is pg.KEYUP and event.key is pg.K_w:
            self.CurWave = Wave(self.waves.popleft())

        '''

        self.check_for_dialogue(surface,keys, current_time)

        self.check_for_end()

        '''
        
        #SWITCH TO DIALOG STATE

        #if keys[pg.K_t] and self.state is not 'DIALOGUE':
            #self.state = 'DIALOGUE'

    def pause(self,surface,keys, current_time):
        '''
        THE PAUSE SCREEN
        '''
        #revise soon
        if 0 < 1:
            pass

        self.draw_level(surface)

    def make_waves(self):
        
        #MAKE SPRITES FOR LEVEL
        
        wave_dict = {c.LEVEL1:'WAVES1',
                     c.LEVEL2:'WAVES2',
                     c.LEVEL3:'WAVES3',
                     c.LEVEL4:'WAVES4',
                     c.LEVEL5:'WAVES5',
                     c.LEVEL6:'WAVES6',
                     c.LEVEL7:'WAVES7',
                     c.LEVEL8:'WAVES8',
                     c.LEVEL9:'WAVES9',
                     c.LEVEL10:'WAVES10'}

        if self.name in wave_dict:
            waves = wave_dict[self.name]
            
            return setup.JSON[waves]

    def transit(self, surface, *args):

        #TRANSITION

        door =  setup.GFX['obj_doors']
        inv_door = pg.transform.flip(door,False,True)
            
        surface.blit(door, (0, -400 + y_pos))
        surface.blit(inv_door, (0, 800 - y_pos))
    
    def dialogue(self, surface, keys, current_time):

        #DIALOG STATE
        
        if keys[pg.K_t] and self.state == 'DIALOGUE':
            self.state = 'NORMAL'

    def check_for_dialogue(self,surface,keys, current_time):
        
        #CHECK FOR DIALOG
        
        pass

    def check_for_end(self):

        #CHECK FOR THE END OF GAME

        pass

    def normal(self,
               surface,
               keys,
               current_time):

        #UPDATE WAVES
             
        self.draw_level(surface)
        self.CurWave.update(surface)
        

class Wave(object):
    #WAVE OBJECT WHICH DETERMINES THE APPERANCE OF ENEMIES
    def __init__(self,
                 group,
                 data):
        super(Wave,
              self).__init__()
        self.data = data.popleft()
        self.members= collect.deque(self.data['members']) 
        self.entry = self.data['begins at']
        self.font = pg.font.Font(setup.FONTS['astron boy wonder'],40)
        self.txt = self.font.render('---INCOMING---',True,c.r)
        self.txt_rect = (self.txt.get_rect())
        self.sprites = group
               
    def countdown(self):

        #COUNTDOWN TO ZERO
        if self.entry:
            self.entry -= 1

    def spawn(self, surface):
        
        #Absulut evil

        if self.members:

            self.Formation = self.members.popleft()

            self.formation = enemies.Formation(self.sprites,
                              self.Formation)

    def update(self, surface):


        #DRAW AND UPDATE SPAWNED ENEMY FORMATIONS

        self.sprites.draw(surface)

        self.sprites.update()
            
        if self.entry:

            #ANNOUNCE WAVE COMMENCE
        
            surface.blit(self.txt,
                     (275 - self.txt_rect.width / 2,
                        400-self.txt_rect.height))
            
            #COUNTDOWN UNTIL APPEARANCE
            
            self.countdown()

        else:

            #APPEAR
            self.spawn(surface)

            self.entry = self.Formation['enters at']


