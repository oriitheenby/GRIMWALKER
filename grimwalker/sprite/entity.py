import sdl2, sdl2.ext

from grimwalker.sprite.sprite import Sprite
from grimwalker.util.signal import Signal, HasSignals

class Entity(Sprite, HasSignals):
	def __init__(self):
		super().__init__()
		self._health = 20

	def change_health(self, val):
		self._health = val
		self.emit("health_change", self._health)

class ThisThing:
	def smth(self, new_hp):
		print(f"signal test new hp: {new_hp}")

ent = Entity()
ahh = ThisThing()
