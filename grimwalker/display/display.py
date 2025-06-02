import sdl2, sdl2.ext

from grimwalker.display.sprite.spriteManager import SpriteManager
from importlib.metadata import version

class GrimDisplayManager:
	def __init__(self, windows: dict = {"main": { "title": f"GRIMWALKER Engine {version("grimwalker")}", "size": (500,500) }} ):
		self._win = {}
		for w in windows:
			win = windows[w]
			print(f"{self._win}\n\n{w}\n\n{windows}")
			self._win.update({w: sdl2.ext.Window(win["title"], win["size"])})
		self.sprite_manager = SpriteManager()
		for w in self._win:
			self.show_window(w)

	def show_window(self, window_id):
		self._win[window_id].show()

__all__ = ["GrimDisplayManager"]