__author__ = 'AFTERCADAVER'

from data.states import store, levels, main_menu, messageScreen,menu
from . import setup, tools
from . import constants as c

MENU     = 'Menu'
menu2     = 'menu'
LEVEL1   = 'level1'
LEVEL2   = 'level2'
LEVEL3   = 'level3'
LEVEL4   = 'level4'
LEVEL5   = 'level5'
LEVEL6   = 'level6'
LEVEL7   = 'level7'
LEVEL8   = 'level8'
LEVEL9   = 'level9'
LEVEL10  = 'level10'
EMAIL    = 'email'
SHOP     = 'shop'
LOADGAME = 'load game'
CREDITS  = 'credits'

def main():
    '''
    Add states to control
    '''
    run_it = tools.control(setup.ORIGINAL_CAPTION)
    
    state_dict = {MENU:main_menu.Menu(),
                  menu2:menu.menu(run_it),
                  LOADGAME:main_menu.loadGame(),
                  LEVEL1:levels.levelState(LEVEL1),
                  LEVEL2:levels.levelState(LEVEL2),
                  LEVEL3:levels.levelState(LEVEL3),
                  LEVEL4:levels.levelState(LEVEL4),
                  LEVEL5:levels.levelState(LEVEL5),
                  LEVEL6:levels.levelState(LEVEL6),
                  EMAIL:messageScreen.email(),
                  SHOP:store.shop()
                    }
    run_it.setup_states(state_dict, c.MENU)
    run_it.main()
