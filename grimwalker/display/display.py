import sdl2, sdl2.ext

from grimwalker.display.sprite.spriteManager import SpriteManager
from importlib.metadata import version
import grimwalker._internal.globals

class GrimDisplayManager:
	def __init__(self, windows: dict = None):
		self._win = {}
		if windows == None:
			windows = {"main": { "title": f"GRIMWALKER Engine {version("grimwalker")}", "size": (500,500) }}
		for w in windows:
			win = windows[w]
			print(f"{self._win}\n\n{w}\n\n{windows}")
			try:
				self._win.update({w: sdl2.ext.Window(win["title"], win["size"])})
			except RuntimeError as e:
				# raise RuntimeError(f"GRIMWALKER Engine {version("grimwalker")} must be initialised before creating windows.")
				grimwalker.internal.globals.raiseError(RuntimeError, "init_for_action", "creating windows.")
		self.sprite_manager = SpriteManager()
		for w in self._win:
			self.show_window(w)

	def show_window(self, window_id):
		self._win[window_id].show()

__all__ = ["GrimDisplayManager"]