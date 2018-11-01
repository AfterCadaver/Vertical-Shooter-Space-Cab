'''
THIS CLASS CONTROLS GUI FOR MESSAGE SCREEN
'''

import pygame as pg
from . import setup
from . import constants as c
from . import tools

class Selector(pg.sprite.Sprite):
    '''
    SELECTOR FOR MENU
    '''
    def __init__(self, info_box):
        super(Selector, self).__init__()
        self.image = pg.Surface((30,30))
        self.rect = self.image.get_rect()
        self.pos_list = []

    def make_state_dict(self):
        '''
        MAKES STATE DICTIONARY
        '''
        state_dict = {
                      }
        return state_dict

    def navigate_select_menu(self):
        pass

    def make_select_menu_pos_list(self):
        '''
        MAKE LIST OF SELECTOR POSITIONS IN SUBMENU
        '''
        pos_list = {(30, 50),
                    (30,100),
                    (30,150)
                    }

    def update(self, pos_index):
        '''
        UPDATE SELECTOR POSITION
        '''

        state_fuction = self.state_dict[self.state]
        state_function(pos_index)

class InfoBox(pg.sprite.Sprite):
    def __init__ (self):
        super(InfoBox, self).__init__()
        self.state = 'info'

    def make_state_dict(self):
        '''
        MAKE STATE METHOD DICITONARY
        '''
        state_dict = {
                      }

        return state_dict

    def show_email_info(self):
        '''
        SHOW INFO ON MESSAGE
        '''
        pass

class MenuGui(object):
    def __init__(self):
        self.infobox = InfoBox()
        self.selector = Selector(self.infobox)
        self.selector_index = 0
        
    def check_for_input(self,keys):
        '''
        CHECKS FOR INPUT
        '''
        if self.allow_input:
            if keys [pg.K_DOWN]:
                pass
            elif keys[pg.K_UP]:
                pass
            elif keys[pg.K_SPACE]:
                pass

    def update(self, keys):
        self.selector.update(self.selector_index)
