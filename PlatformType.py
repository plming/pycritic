from enum import Enum
from enum import unique


@unique
class PlatformType(Enum):
    PC = 'pc'
    SWITCH = 'switch'
    WII_U = 'wii-u'
    WII = 'wii'
    GAMECUBE = 'gamecube'
    N64 = 'nintendo-64'
    N3DS = '3ds'
    NDS = 'ds'
    GBA = 'game-boy-advance'
    PS5 = 'playstation-5'
    PS4 = 'playstation-4'
    PS3 = 'playstation-3'
    PS2 = 'playstation-2'
    PS = 'playstation'
    PS_VITA = 'playstation-vita'
    PSP = 'psp'
    XSX = 'xbox-series-x'
    XO = 'xbox-one'
    XBOX = 'xbox'
    STADIA = 'stadia'
    IOS = 'ios'
    DREAMCAST = 'dreamcast'
