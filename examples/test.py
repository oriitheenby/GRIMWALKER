import grimwalker as gw

gw.init()

gw.displayManager.show_window(window_id="main")
while gw.running:
	print(gw.running)
	for e in gw.event.get_events():
		if e.type == gw.event.EventType.QUIT:
			gw.running(False)