import pygame as pg
import collections as collect
import json, math, random
from data import setup
from data import constants as c


class Enemy(pg.sprite.Sprite):
    def __init__(self,
                 name,
                 Group,
                 state='none',
                 mode='server'):
        #GENERIC CLASS FOR ALL ENEMIES
        super(Enemy,
              self).__init__()
        pg.sprite.Sprite.__init__(self, Group)
        self.state, self.name, self.mode, self.group = state, name, mode, Group
        
        self.image        = setup.GFX[name]
        self.rect         = self.image.get_rect()
        self.rect.y       = (-self.rect.height)

        self.statedict    = self.choose_state()
        
        self.speedx, self.speedy, self.rate = 0, 0, 2
        
        self.azimuth, self.spacing, self.number, self.amplitude=  275, 0, 0, 30
        self.shield       = 0
        self.progression  = 0
        
        self.acceleration = 0
        self.counting     = 10
        self.fresh = 1

    def choose_mode(self):
        #CREATE STATE DICT OF POSSIBLE ENEMY ATTTACK BEHAVIORS

        mode_dict ={'server':self.server,
                    'turret':self.turret,
                    }

        return mode_dict

    def choose_state(self):
        #CREATE STATE DICT OF POSSIBLE ENEMY STATES
        
        statedict ={'sine'       :self.sine,
                    'charging'   :self.charging,
                    'charging2'  :self.charging_2,
                    'infmovement':self.infMovement,
                    'bouncing'   :self.bouncing,
                    'kamikaze'   :self.kamikaze,
                    'orbit'      :self.orbit,
                    'none'       :self.basicMovement
                    }
        
        return statedict

    def orbit(self):
        #HAVE SHIPS ORBIT AROUND IMAGINARY POINT

        self.progression += self.speedy

        #MOVE AT DIFFERENT RATES TO APPROXIMATE INFINITY SYMBOL

        self.rect.centerx = 100 * math.sin(self.progression / 2 * math.pi / 30) + 275        

    def sine(self):

        #TIE X-AXIS TO A SINE WAVE

        self.basicMovement()

        self.progression += 1
        this = self.progression / 2 * math.pi / self.amplitude
        distance = self.azimuth + self.spacing
        
        self.rect.centerx = self.azimuth * math.sin(this) + distance

    def bouncing(self):

        #MOVE IN A SINE WAVE UP AND DOWN

        self.progression += self.speedy
        this = self.progression / 2 * math.pi / self.amplitude
        distance = 100 + self.spacing
        
        self.rect.centery = self.azimuth * math.sin(this) + distance

    def basicMovement(self):

        #MOVE

        self.rect.y += self.speedy
        self.rect.x += self.speedx

    def charging(self):

        #CHARGE STAGE 1

        self.basicMovement()

        '''
        if self.rect.y >= 400:
            self.speedy = -self.speedy
 
            self.state = 'charging2'
        '''

    def charging_2(self):

        #CHARGING STAGE 2

        self.basicMovement()

        if not self.counting:
            self.acceleration += 1
            self.counting = 10

        else:
            self.counting -= 1

        if self.rect.y <= 100:
            self.speedy = self.acceleration

    def turret(self):
        
        #START A COUNTDOWN, SHOOT, FIRE, AND REPEAT

        slow = 30
        medium = 20
        fast = 10
        
        if not self.counting:
            A = Attack(self.name[:-2],
                       self.group,
                       self.rect.center,
                       state='homing')

            self.counting = medium

        if self.counting:
            self.counting -= 1

    def server(self):
        #SHOOT AT A FIXED RATE

        if not self.counting:
            A = Attack(self.name[:-2],
                       self.group,
                       self.rect.center,
                       state='move')

            self.counting = self.speedy * 10
        else:
            self.counting -= 1
            
    def kamikaze(self):
        pass
    
    def infMovement(self):
        
        self.progression += self.speedy

        #MOVE AT DIFFERENT RATES TO APPROXIMATE INFINITY SYMBOL

        self.rect.centerx = 275 * math.sin(self.progression / 2 * math.pi / 60) + 275
        self.rect.centery = 100 * math.sin(self.progression / 2 * math.pi / 30) + 200

    def update(self):
        if self.rect.top >= 800:
            self.kill()

        state_func = self.choose_state()[self.state]
        mode_func  = self.choose_mode()[self.mode]
        state_func()
        mode_func()

class Attack(pg.sprite.Sprite):
    def __init__(self,
                 name,
                 group,
                 coords=(0,0),
                 state='move',
                 dmg=5,
                 target=(50,700),
                 firing_left=False):
        super(Attack,
              self).__init__()
        pg.sprite.Sprite.__init__(self,
                                  group)
        self.image = pg.Surface((10,10))
        self.image.fill(c.w)
        self.rect = self.image.get_rect()

        self.number = 0

        self.state = state
        self.speedx, self.speedy = 20, 20
        self.rect.center = coords

        self.progression = 0

        self.azimuth, self.spacing, self.amplitude =  275, 0, 30

        self.t_position = target
        self.vector = self.calc_vec(self.t_position)

    def set_sine(self):
        pass

    def set_direction(self,
                      speed):

        if self.firing_right:
            speed = -speed

        return speed

    def setup_behaviors(self):
        #SETUP THE POSSIBLE STATES OF THE PROJECTILE

        behaviors_dict = {'move'  :self.move,
                          'homing':self.homing,
                          'sine'  :self.sine,
                          'mines' :self.mines
                         }

        return behaviors_dict

    def sine(self):
        #TIE X-AXIS TO A SINE WAVE

        self.rect.y += self.speedy

        self.progression += 1
        this = self.progression / 2 * math.pi / self.amplitude
        distance = self.azimuth + self.spacing
        
        self.rect.centerx = self.azimuth * math.sin(this) + distance

    def calc_vec(self,
                 coords):
        #CALCULATE VECTOR
        
        this =  coords[0] - self.rect.center[0]
        that =  coords[1] - self.rect.center[1]

        return pg.math.Vector2(this, that).normalize()
    
    def mines(self,
              *args):
        
        #MINE BEHAVIORS
        pass

    def move(self,
             *args):
        #move 
        self.rect.y += self.speedy

    def homing(self,
               *args):
        #HOME IN ON TARGET WITHOUT UPDATING VECTOR

        self.rect.centerx += self.vector[0] * self.speedx
        self.rect.centery += self.vector[1] * self.speedy

    def counter(self): 
        if self.number >= 30:
            self.kill()

        else:
            self.number += 1

    def update(self,
               *args):

        this_func = self.setup_behaviors()[self.state]
        this_func(*args)
        self.counter()

class Formation(object):
    def __init__(self,
                 group,
                 data):
        super(Formation,
              self).__init__()
        self.sprites = group
        self.dict = self.formation_dict()
        self.Func = self.dict[data['formation']]
        self.Func(data)

    def choose_speed(self):
        #SET SPEED BY KEYWORD

        speed_dict={'zero'     :0,
                    'slow'     :2,
                    'medium'   :5,
                    'fast'     :7,
                    'very fast':10,
                    'ludicrous':12}
        
        return speed_dict

    def choose_proximity(self):

        #

        spacing_dict={'tight' :10,
                      'medium':40,
                      'loose' :70}

        return spacing_dict

    def formation_dict(self):

        #CREATE DICT FOR SUBTYPES OF FORMATIONS

        form_dict={'v'         :self.v_formation,
                   'vertical'  :self.vertical_formation,
                   'horizontal':self.horizontal_formation,
                   'jagged'    :self.jagged_formation,
                   'circle'    :self.circle_formation,
                   'this'      :self.this_formation,
                   'place'     :self.placeholder}
        
        return form_dict

    def v_formation(self,
                    data,
                    *args):
        
        #ARRANGE SHIPS IN V-SHAPE
        
        position = 0
        spacing = 0

        for members in range(data['number']):
            e = Enemy(data['ship'],
                      self.sprites,
                      state=data['state'],
                      mode=data['mode'])

            e.rect.x += data['x_axis'] + position

            #e.spacing = position
        
            if members < (data['number'] - 1) / 2:
                e.rect.y += spacing

                spacing += data['spacing']

            else:
                e.rect.y += spacing

                spacing -= data['spacing']
    
            e.speedy = self.choose_speed()[data['speed']]

            e.progression += position

            position += data['spacing'] + e.rect.width / 8

    def horizontal_formation(self,
                             data,
                             *args):
        
        #ARRANGE SHIPS IN LINE
        
        position = 0

        for members in range (data['number']):
            e = Enemy(data['ship'],
                      self.sprites,
                      state=data['state'],
                      mode=data['mode'])
            
            e.rect.centerx = e.rect.width + position
    
            e.speedy = self.choose_speed()[data['speed']]

            position += data['spacing'] 

    def vertical_formation(self,
                           data,
                           *args):
        
        #ARRANGE SHIPS IN LINE
        
        position = 0

        for members in range (data['number']):
            e = Enemy(data['ship'],
                      self.sprites,
                      state=data['state'],
                      mode=data['mode'])
            
            e.rect.centery = e.rect.height - position

            e.rect.x = data['x_axis']

            e.progression += position / 8
    
            e.speedy = self.choose_speed()[data['speed']]

            position += data['spacing']

    def jagged_formation(self,
                         data,
                         *args):
        #ARRANGE SHIPS IN JAGGED SHAPES
        
        position = 0

        for ships in range(data['number']):
            e = Enemy(data['ship'],
                      self.sprites,
                      state=data['state'],
                      mode=data['mode'])
            
            e.rect.y -= position

            if ships % 2 == 0:
                e.rect.x = 0 + data['spacing']

            if ships % 2 == 1:
                e.rect.x = 275 - e.rect.width - data['spacing']

            e.speedy = self.choose_speed()[data['speed']]

            position += data['spacing']

    def circle_formation(self,
                         data,
                         *args):
        #ARRANGE SHIPS IN CIRCLE
        pass
    
    def wheel_formation(self,
                        data,
                        *args):
        #ARANGE SHIPS IN A CIRCLE
        pass
    
    def placeholder(self,
                    data,
                    *args):
        pass


    def this_formation(self,
                       data):
        pass

