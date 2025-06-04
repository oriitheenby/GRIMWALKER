# import sdl2, sdl2.ext

from .grimwalker import gw
from importlib.metadata import version, PackageNotFoundError
from .logic import event
from .globals_ import *

for attr in dir(gw):
    if attr.startswith("_"): # and callable(getattr(gw, attr))
        pass
    else:
        globals()[attr] = getattr(gw, attr)
print("GLOBALS BITCH:", globals())

try:
    __version__ = version("grimwalker")
except PackageNotFoundError:
    __version__ = "unknown"