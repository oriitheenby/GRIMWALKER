import grimwalker as gw

gw.init()


while gw.running():
	print(gw.running())
	gw.displayManager().show_window(gw.displayManager(), window_id="main")
	for e in gw.event.get_events():
		if e.type == gw.event.EventType.QUIT:
			gw.running(False)