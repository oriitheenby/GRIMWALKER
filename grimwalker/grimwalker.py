import sdl2, sdl2.ext
from grimwalker import display
from grimwalker.util.registry import Registry
import grimwalker._internal.globals as internal
from grimwalker.util.signal import Signal
from grimwalker.sprite.entity import Entity, ThisThing

class Grimwalker:
	def __init__(self):
		self._displayManager = None
		self._registry = None
		self._running = None
		self.ent = Entity()
		self.this_thing = ThisThing()

	def init(self):
		sdl2.ext.init()
		self._displayManager = display.GrimDisplayManager()
		self._registry = Registry()
		self.ent.connect("health_change", self.this_thing.smth)
		self.ent.change_health(15)
		self._running = True

	@property
	def displayManager(self):
		if self._displayManager == None:
			internal.raiseError(AttributeError, "init_for_action", "accessing Grimwalker.displayManager")
		return self._displayManager
	
	@displayManager.setter
	def displayManager(self):
		raise AttributeError()

	@property
	def registry(self):
		return self._registry
	
	@registry.setter
	def registry(self, val):
		# TODO: once logger set up, print a warning
		# (also check if this applies to changing things INSIDE the registry and not just the overall reg variable itself)
		self._registry = val

	@property
	def running(self):
		return self._running
	
	@running.setter
	def running(self, val):
		self._running = val


gw = Grimwalker()