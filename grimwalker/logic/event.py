import sdl2, sdl2.ext
from enum import Enum

def get_events():
	return sdl2.ext.get_events()

class EventType(Enum):
	QUIT = sdl2.SDL_QUIT