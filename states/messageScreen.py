__author__ = 'AFTERCADAVER: pleas give me FEED BACK!!'

import json
import collections as collect
import pygame as pg
from .. import setup, tools, menugui, shopgui, textbox
from .. import constants as c

'''
EMAIL GUI CLASS
'''

class email(tools.State):
    
    #THE STATE FOR THE EMAILSCREEN
    
    def __init__(self):
        super(email,
              self).__init__()
        self.music = setup.MUSIC['chamber danger']
        self.volume = 0.4
        self.next = c.LEVEL1
        self.font = pg.font.Font(setup.FONTS['cour'],25)

    def get_emails(self):
        
        #MAKE SPRITES FOR LEVEL
        
        email_dict = {'level1':'EMAIL1',
                      'level2':'EMAIL2',
                      'level3':'EMAIL3'}

        if self.name in email_dict:
            emails = email_dict[self.name]
            
            return setup.JSON[emails]

    def sad(self,
            directory,
            accept=('.json')):

        emails = {}
        
        for email in os.listdir(directory):
            name, ext = os.path.splitext(email)
            if ext.lower() in accept:
                emails[name] = os.path.join(directory, emails)

        return emails
    
    def startup(self,
                current_time,
                game_data):

        self.allow_input = False
        
        self.state = c.NORMAL
        self.state_dict = self.make_state_dict()
        self.game_data = game_data

        self.name = self.game_data['last level']

        self.index = 0

        self.width = 80

        self.list = self.json_reader(self.get_emails())
        self.pos = self.make_height_list(self.list)
        self.selector_height = self.pos[self.index]
        self.selected_item = self.list[self.index]

        self.gui = shopgui.Gui(self)

    def make_height_list(self, this_list):

        #GENERATE AND RETURN A LIST OF HEIGHTS FOR EMAIL ITEMS

        that = []

        value = 15

        for e in this_list:
            that.append(value)

            value += 80

        return that

    def draw_level(self,
                   surface):

        #DRAW THE LEVEL
        
        surface.fill(c.b)

        y = 20

        avatar_height = 20

        surface.blit(self.font.render('[x]BACK',
                                      True,
                                      c.w),
                                      (50, 750))

        #DRAW THE GUI SELECTOR IN SPECIFIC

        self.gui.draw(surface)

        #FIRST LOOP THROUGH LIST FOR EACH EMAIL

        for emails in self.list:

            #SECOND, BLIT THEM AT INCREMENTS OF 80 

            surface.blit(setup.GFX['chr ' + emails['chr']],
                        (20, y))

            #NEXT, BLIT THE EMAIL HEADERS
            
            surface.blit(self.font.render(emails['header'],
                                          True,
                                          emails['color']),
                                          (100, y))

            #FINALLY,INCREASE INCREMENT

            y += 80
        
    def email(self,
              surface,
              keys,
              current_time):

        if self.allow_input:

            # X IF FINISHED READING
            
            if keys[pg.K_x]:
                self.state = c.NORMAL
                self.allow_input = False

        if not keys[pg.K_x]:
            self.allow_input = True

        self.draw_level(surface)

        #USE DATA IN DICTIONARIES TO SPECIFY HEADER TEXT, TEXT, AND COLOR

        this = textbox.emailBox(self.selected_item['header'],
                                self.selected_item['text'],
                                self.selected_item['color'])

        surface.blit(this.image,(25,25))
                    
    def make_state_dict(self):
        
        #MAKE DICTIONARY OF STATES IN LEVEL
        

        state_dict = {c.TRANSITION:self.transition,
                      'EMAIL':self.email,
                      c.NORMAL:self.normal_update
                     }
        
        return state_dict
    
    def update(self,
               surface,
               keys,
               current_time):

        #UPDATE
        update_level = self.state_dict[self.state]
        update_level(surface, keys, current_time)
        
    def normal_update(self,
                      surface,
                      keys,
                      current_time):

        #SET CONTROLS HERE

        if self.allow_input:
            if keys[pg.K_UP]:
                self.index += -1
                self.allow_input = False

            if self.index < 0 and keys[pg.K_UP]:
                self.index += len(self.list)
                self.allow_input = False

            if keys[pg.K_DOWN]:
                self.index += 1
                self.allow_input = False

            if self.index > len(self.list) - 1 and keys[pg.K_DOWN]:
                self.index += -len(self.list)
                self.allow_input = False

        #SELECT EMAIL AND ENTER 'EMAIL STATE' WITH Z

            if keys[pg.K_z]:
                self.state = 'EMAIL'
                self.allow_input = False

            if keys[pg.K_x]:
                self.next = 'menu'
                self.allow_input = False
                self.done = True
                

        if not keys[pg.K_DOWN] and not keys[pg.K_UP] and not keys[pg.K_z] and not keys[pg.K_x]:
            self.allow_input = True

        self.draw_level(surface)

        self.selected_item = self.list[self.index]

        self.gui.selector.rect.y = self.pos[self.index]

    def transition(self):
        pass

