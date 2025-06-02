# import sdl2, sdl2.ext

from .grimwalker import *
from importlib.metadata import version, PackageNotFoundError
from .logic import event

try:
    __version__ = version("grimwalker")
except PackageNotFoundError:
    __version__ = "unknown"