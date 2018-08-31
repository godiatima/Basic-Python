import vlc
import MediaPlayer

player = vlc.MediaPlayer("/home/godfrey/Music/steghide.mp3")

player.play()

playlist = [ '/home/godfrey/Music/steghide.mp3', '/home/godfrey/Music/sample.mp3' ]

for song in playlist:
	player = vlc.MediaPlayer(song)
	player.play()
