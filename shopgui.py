import json
import pygame as pg
from . import setup, textbox
from . import constants as c

class Gui(object):
    '''
    CLASS FOR GUI OF SHOP STATE
    '''
    def __init__(self, level):
        self.level = level
        self.allow_input = False
        self.selector = textbox.Selector(level.width)
        self.selector.rect.topleft = (0,level.selector_height)

    def make_dialog_box(self, dialog_list, index):
        #image = setup.GFX['']
        pass

    def display_money(self, surface):
        #BLIT MONEY ONTO SURFACE

        #surface.blit(self.game_data['points'],())
        pass

    def make_state_dict(self):
        '''
        MAKE STATE DICTIONARY FOR GUI BEHAVIOUR
        '''
        state_dict = {'dialog':self.control_dialog,
                      'buy':self.buy
                      }
        
        return state_dict

    def control_dialog(self):
        pass

    def buy(self):
        pass

    def reject_insufficient_money(self,
                                  keys,
                                  current_time):
        pass

    def update(self, keys,current_time):
        '''
        UPDATE SHOPGUI
        '''
        state_function = self.state_dict[self.state]
        state_function(keys, current_time)
        

    def draw(self, surface):
        '''
        DRAW GUI TO LEVEL SURFACE
        '''

        state_list = []

        surface.blit(self.selector.image, self.selector.rect)
    
    
    
        
