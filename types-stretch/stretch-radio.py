from dataclasses import dataclass
import math

# this should be a free function to allow for reuse across unrelated classes
# this functionality should only be implemented once
def format(time: int) -> str:
    mm = math.floor(time / 60)
    ss = time % 60
    return f"{mm}:{ss:02}"

@dataclass(frozen=True)
class Person:
	name: str
	# they can add other fields that make sense
	def __str__(self):
		return self.name

@dataclass(frozen=True)
class Song:
	artist: Person
	duration: int
	title: str

	def __str__(self):
		return f"{str(self.artist)} - {self.title} ({format(self.duration)})"

@dataclass(frozen=True)
class TalkShow:
	host: Person
	guests: list[Person]
	duration: int
	title: str
	def __str__(self):
		guests = ", ".join([str(guest) for guest in self.guests])
		return f"{str(self.host)} with {guests} - {self.title} ({format(self.duration)})"
 
@dataclass(frozen=True)
class Podcast(TalkShow):
	sponsor: str
 
	def __str__(self):
		return super().__str__() + f" sponsored by {self.sponsor}"
	# they should not re-implement the super call here
 
# At a minimum they should implement the following
@dataclass
class Playlist[T]:
	items: list[T]
	currently_playing_index: int
    
	def __init__(self, items):
		self.items = items
		self.currently_playing_index = 0

	def play_next(self):
		self.currently_playing_index = (self.currently_playing_index + 1) % len(self.items)

	def get_currently_playing(self):
		return self.items[self.currently_playing_index]

	# it's fine if they change it from an int to return the formatted str
	def get_total_duration(self) -> str:
		list_duration: int = 0
		for item in self.items:
			# It is deliberately ambiguous how they should handle duration
			# given some of the classes are not related but they all implement it
			list_duration += item.duration
		return format(list_duration)

astley = Person(name="Rick Astley")
song_a = Song(astley, 210, "Never Gonna Give You Up")

psy = Person(name="Psy")
song_b = Song(psy, 219, "Gangnam Style")
funny_songs = Playlist[Song]([song_a, song_b])
print(funny_songs.get_currently_playing())
funny_songs.play_next()
print(funny_songs.get_currently_playing())
funny_songs.play_next()
print(funny_songs.get_currently_playing())
print(funny_songs.get_total_duration())

bragg = Person(name="Melvyn Bragg")
al_khalili = Person(name="Jim Al-Khalili")
rowan = Person(name="Sheila Rowan")
crawford = Person(name="Carolin Crawford")
show_a = TalkShow(host=bragg, guests=[al_khalili, rowan, crawford], duration=2700, title="Gravitational Waves")
print(show_a)

mcculloch = Person(name="Gretchen McCulloch")
smith_galer = Person(name="Sophia Smith Galer")
pod_a = Podcast(host=mcculloch, guests=[smith_galer], duration=3000, title="How (not) to kill a language", sponsor="Patreon")
print(pod_a)