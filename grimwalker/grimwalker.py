import sdl2, sdl2.ext
from grimwalker import display
from grimwalker.util.registry import Registry

_displayManager = display.GrimDisplayManager
_registry = Registry()
_running = None

def displayManager():
	if _displayManager != None:
		return _displayManager
	else:
		raise AttributeError("GRIMWALKER must be initialised before you can access the displayManager")

def running(val=None):
	if val:
		_running = val
	else:
		try:
			return _running
		except UnboundLocalError:
			return True

def init():
	_running = True
	sdl2.ext.init()
	# _displayManager = display.GrimDisplayManager()
	# _registry = Registry()

class Grimwalker:
	def __init__():
		self._displayManager = display.GrimDisplayManager()
		self._registry = Registry()
		self._running = False

	@property
	def displayManager(self):
		return self._displayManager
	
	@displayManager.setter
	def displayManager(self):
		raise AttributeError("Grimwalker.displayManager is immutable.")

	@property
	def registry(self):
		return self._registry
	
	@registry.setter
	def registry(self, val):
		# TODO: once logger set up, print a warning
		# (also check if this applies to changing things INSIDE the registry and not just the overall reg variable itself)
		self._registry = val