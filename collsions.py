import pygame as pg

class collisionHandler:
    '''
    collisions between characters
    '''
    def __init__(self, player, blocker, sprites, portals, level):
        self.player = player
    def make_blocker_list(self, blockers, sprites):
        '''
        return list of collisions
        '''
        blocker_list = []

        for blocker in blockers:
            blocker_list.append(blocker)

        for sprite in sprites:
            blocker_list.extend(sprite.blockers)

    def check_for_blockers(self):
        '''
        '''
        for blocker in self.blocker:
            if self.player.rect.colliderect(blocker)
                player_collided = True
        
        
