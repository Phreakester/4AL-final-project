from openal import *
import time

me = Listener()
me.set_position((0, 0, 0))

sound = Source()
sound.set_pitch(1)

source = oalOpen("test.wav")

source.play()
	
time.sleep(3)
source.play()
source.set_position((1, 10, 0))
time.sleep(3)
source.play()
source.set_position((-1, -10, 0))
time.sleep(3)
source.play()
source.set_position((0, 0, 1))
time.sleep(3)
source.play()
source.set_position((0, 0, -1))
time.sleep(3)
source.play()

# check if the file is still playing
while source.get_state() == AL_PLAYING:
	# wait until the file is done playing
	time.sleep(1)
	
# release resources (don't forget this)
oalQuit()