import sdl2, sdl2.ext

from collections import defaultdict

class Signal:
	def __init__(self):
		self._slots = []

	def connect(self, callback):
		self._slots.append(callback)

	def disconnect(self, callback):
		self._slots.remove(callback)

	def emit(self, *args):
		for callback in self._slots:
			print(f"ARGS: {args}\n\n\n\n")
			callback(args)

class HasSignals:
	def __init__(self):
		self._signals = defaultdict(Signal)

	def connect(self, signal_name, callback):
		self._signals[signal_name].connect(callback)

	def disconnect(self, signal_name, callback):
		self._signals[signal_name].disconnect(callback)

	def emit(self, signal_name, callback):
		self._signals[signal_name].emit(callback)