__author__ = 'AFTERCADAVER'

import pygame as pg
from . import setup, tools
from . import constants as c

class Selector(pg.sprite.Sprite):
    '''
    asdsad
    '''
    def __init__(self,
                 width):
        super(Selector,
              self).__init__()
        self.image = pg.Surface((550,width))
        self.rect = self.image.get_rect()
        self.image.fill(c.g)

class emailBox(object):
    #dfsdfdsfs
    def __init__(self,
                 header,
                 text,
                 color):
        self.image = pg.Surface((500,750))
        self.image.fill(c.b)
        self.rect = self.image.get_rect()
        self.font = pg.font.Font(setup.FONTS['cour'],18)
        self.header = pg.font.Font(setup.FONTS['cour'],24)

    #CHANGE THIS
        self.message = text

        header = self.header.render(header,
                                  False,
                                  color)

        self.image.blit(header,
                        (250 - header.get_size()[0]/ 2, 10))
        
        blit_text(self.image,
                  self.message,
                  (50,50),
                  self.font,
                  color)
    
def blit_text(surface,
              text,
              pos,
              font,
              color=(0,0,0)):
    
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row. 

class textHandler:
    '''
    HANDLES INTERACTION BETWEEN SPRITES TO CREATE TEXT BOXES
    '''

    def __init__(self,
                 level):
        self.player = level.player
        self.sprites = level.sprites
        self.textbox = None
        self.level = level
        self.game_data = level.game_data

    def update(self,
               keys,
               current_time):
        '''
        CHECKS FOR THE CREATION OF TEXTBOXES
        '''
        if keys[pg.K_SPACE] and not self.textbox and self.allow_input:
            for sprite in self.sprites:
                if (current_time - self.last_textbox_timer) > 300:
                    pass
                    
        if self.textbox:

            self.textbox.update(keys, current_time)

            if self.textbox.done:
           
                    if self.text.box.index < (len(self.textbox.text_list)- 1):

                        index = self.textbox.index + 1
                        dialogue = self.textbox.text_list
                        if self.textbox.name == 'dialoguebox':
                            pass
                        
                    elif 3 == 3:
                        pass
                    elif self.talking_sprite == 'BRAKAR':
                        if self.game_data['B1_ALIVE']:
                            dialogue = ['Hey, remember me?...',
                                        'Is that Brakar ? ... Oh no...',
                                        ' Sorry, I don\'t want any trouble...',
                                        'You should\'nt piss off the boss! Ha Ha!'
                                        ]
                        elif self.game_date['B1_DEAD']:
                            dialogue = ['Wait, wait, I was\'nt ready!']
    
                    elif self.talking_sprite == 'BRAKAROO':
                        if self.game_data['B2_ALIVE']:
                            dialogue = ['how\'s the new job...?',
                                        'bounty hunter to caby! Ha,ha...',
                                        '...',
                                        'No. I would be if I was in a taxi job'
                                        ]
                        elif self.game_data['B2_DEAD']:
                            dialogue = ['AAAAAA!!!!!! You jerk! Thrash is coming for you...']
                            
                    elif self.talking_sprite == 'BRABEE':
                        if self.game_data['B3_ALIVE']:
                            dialogue = ['Hey can we not fight.please,please!',
                                        'We just go and you can pretend that i did kill you...',
                                        'all fine with me...',
                                        'can i ask of something ples...',
                                        'Yes?',
                                        'I dont want to piss off the boss',
                                        'Could you he beat me up alittle please?',
                                        'Sigh fine'
                                        ]
                    elif self.talking_sprite == 'ANCIENT':
                        if self.game_data['B4_ALIVE']:
                            pass
                        elif self.game_data['B4_DEAD']:
                            dialogue = ['01101001 01101110 01110100 01110010 01110101 01100100 01100101 01110010 01110011',
                                        '00100000 01110111 01100001 01110010 01101110 01101001 01101110',
                                        '01100111 00100000 01110100 01101111 00100000 01100010 01101111 01110011 01110011 00001101 00001010 00001101 00001010'


                                        ]
                    elif self.talking_sprite == 'THODEROR':
                        if self.game_data['B5_ALIVE']:
                            dialogue = ['Hey, hey hey!',
                                        'i dont have time for this',
                                        'wait i have a ridel',
                                        'What is a man that has to many weapons...',
                                        'and has a big ego...',
                                        'and owns a lucrative business...',
                                        ' you...',
                                        'Nnnn... hmmmm... eeeee...',
                                        'hmm...',
                                        'I was going to say \'you\' but that\'s good to...'
                                        ]

                        elif self.game_data['B5_DEAD']:
                            dialogue = ['i am dying.peace out the universe']

        if not keys[pg.K_SPACE]:
            self.allow_input = True

    def end_dialogue(self,
                     current_time):
        '''
        END DIALOGUE STATE FOR LEVEL
        '''
        pass
    def check_for_dialogue(self,
                           sprite):
        '''
        CHECKS IF SPRITE IS ABLE TO SPEAK
        '''
        pass
    
    def draw(self,
             surface):
        '''
        DRAW TEXTBOX
        '''
        
        if self.textbox:
            surface.blit(self.textbox.image, self.textbox.rect)

            
        

    
        
                    
                    
                    
                
