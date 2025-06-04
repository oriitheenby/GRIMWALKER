from importlib.metadata import version

_errors = {
	"init_for_action": "GRIMWALKER Engine {ver} must be initialised before {action}."
}

def raiseError(type: Exception, messagetype, action_name=None):
	if messagetype in _errors:
		if action_name:
			text = _errors[messagetype]
			try:
				text.format(ver=version("grimwalker"), action=action_name)
			except KeyError:
				raise type(text.format(ver=version("grimwalker")))