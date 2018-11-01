__author__ = 'kennichinitta'

import pygame as pg
import collections as collect
import os, json
from . import constants as c

class control:
    '''
    control class for the entire project.
    Contains game loop,
    event loop.
    logic for flipping states here.
    '''
    def __init__(self, caption):
        self.screen = pg.display.get_surface()
        self.done = False
        self.clock = pg.time.Clock()
        self.caption = caption
        self.fps = 60
        self.show_fps = False
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self.state, self.state_dict = None, {}
        self.state_name = None
        

    def change_music(self):
        '''
        Set music for new state
        '''
        if self.state.music_title == self.state.previous_music:
            pass
        elif self.state.music:
            pg.mixer.music.load(self.state.music)
            pg.mixer.music.set_volume(self.state.volume)
            pg.mixer.music.play(-1)
            
    
    def event_loop(self):
        self.events = pg.event.get()

        for events in self.events:
            if events.type == pg.QUIT:
                self.done = True

            elif events.type ==pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                self.toggle_show_fps(events.key)
                self.state.get_event(events)

            elif events.type ==pg.KEYUP:
                self.keys = pg.key.get_pressed()
                self.state.get_event(events)

    def flip_state(self):
        persist = self.state.cleanup()
        previous, self.state_name = self.state_name, self.state.next
        previous_music = self.state.music_title
        self.state = self.state_dict[self.state_name]
        self.state.previous = previous
        self.state.previous_music = previous_music
        self.state.startup(self.current_time, persist)
        self.change_music()

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
        self.change_music()

    def toggle_show_fps(self, key):
        '''
        toggles FPS display
        '''
        if key == pg.K_F5:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pg.display.set_caption(self.caption)

    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)
            if self.show_fps:
                fps = self.clock.get_fps()
                with_fps = '{} - {:2f} FPS'.format(self.caption, fps)
                pg.display.set_caption(with_fps)

    def update(self):
        '''
        UPDATE THE GAME
        '''

        self.current_time = pg.time.get_ticks()
        if self.state.quit:
            self.done = True

        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)
        
class State:
    '''
    GAME STATES
    '''
    def __init__(self):
        self.start_time, self.current_time = 0.0, 0.0
        self.done, self.quit = False, False
        self.next, previous = None, None
        self.game_data = {}
        self.music = None
        self.music_title = None
        self.previous_music = None

    def get_event(self, event):
        pass

    def startup(self, current_time, game_data):
        self.start_time = current_time
        self.game_data = game_data

    def cleanup(self):
        self.done = False
        return self.game_data
    
    def update(self, surface, keys, current_time):
        pass

    def json_reader(self, json_file):
        #READ AND EXTRACT DATA FROM MULTIPLE JSON OBJECTS INTO LIST
        
        json_list = collect.deque([])
        with open(json_file) as f:
            for line in f:
                while True:
                    try:
                        jfile = json.loads(line)
                        break
                    except ValueError:
                        # Not yet a complete JSON value
                        line += next(f)
                # do something with jfile
                json_list.append(jfile)
        return json_list
    
def set_music(directory, accept=('.wav', '.mp3', '.ogg', '.midi')):
    '''
    asdad
    '''
    songs = {}
    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs
            
def set_gfx(directory, colorkey= (123, 45, 78), accept=('.png','.jpg','.bmp')):
    '''
    load all the graphics
    '''
    pics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            pics[name] = img
    return pics
    
def set_sfx(directory, accept=('.wav', '.mp3', 'ogg', '.midi')):
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects

def load_json(directory, accept=('.json')):
    '''
    load all json files
    '''
    json_files = {}

    for files in os.listdir(directory):
        name, ext = os.path.splitext(files)
        if ext.lower() in accept:
            json_files[name] = os.path.join(directory,files)
    return json_files

def set_fonts(directory, accept=('.ttf')):
    return set_music(directory,accept)

def get_image(x,y,width,height,sheet):
    '''
    get image from sprite sheet
    '''
    image = pg.Surface([width,height])
    rect = image.get_rect()

    image.blit(sheet,(0,0),(x,y,width,height))
    image.set_colorkey(c.b)

def setup_states(self, state_dict, start_dict):
    self.state_dict = state_dict
    self.state_name = start_state
    self.state_name = self.state_dict[self.state_name]
    self.set_music()

def create_game_data_dict():


    data_dict = {
       "assist present": False,
       "game complete": False,
       "hp maximum": 100,
       "last level": "level1",
       "points": 0,
       "quest1 complete": False,
       "quest2 complete": False,
       "quest3 complete": False,
       "quest4 complete": False,
       "reg rate": 5,
       "ship max speed": 10,
       "volume": 0.1,
       "weapon equipped": "joy"
}

    return data_dict 
