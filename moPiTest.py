from mpd import MPDClient

client = MPDClient()

client.timeout = 15
client.idletimeout = None
client.connect("localhost", 6600)

client.add("spotify:track:6FMtZ1U2A9aq9t5jOHiOEU")
client.play()

client.close()
client.disconnect()
