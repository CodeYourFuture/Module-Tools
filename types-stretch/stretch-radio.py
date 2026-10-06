class Song:
	def __init__(self, artist, duration, title):
		self.artist = artist # should be a string
		self.duration = duration # should be an integer in seconds
		self.title = title # should be a string

	def __str__(self):
		return f"{self.artist} - {self.title} ({self.duration})"

class TalkShow:
	def __init__(self, host, guests, duration, title):
		self.host = host # should be a string
		self.guests = guests # should be a list of strings
		self.duration = duration # should be an integer in seconds
		self.title = title # should be a string

class Playlist:
	def __init__(self, items):
		self.items = items # A list of Song or TalkShow
		self.currently_playing_index = 0

	def play_next(self):
		pass
		# TODO: increment the currently_playing_index, when you get to the end loop back to 0

	def get_currently_playing(self):
		return "todo"
		# TODO: return a string representation of whatever is playing at the current index
		# See the __str__ method in Song for an example of how to make a string representation of a class

	def get_total_duration(self):
		return 0
		# TODO: return

song_a = Song("Rick Astley", 210, "Never Gonna Give You Up")
print(song_a)

song_b = Song("Psy", 219, "Gangnam Style")
funny_songs = Playlist([song_a, song_b])
print(funny_songs.get_currently_playing())

show_a = TalkShow("Melvyn Bragg", ["Jim Al-Khalili", "Sheila Rowan", "Carolin Crawford"], 2700, "Gravitational Waves")

