from openal import *

import time
import random
import numpy as np

source = oalOpen('a4.wav')


right = (1, 0, 0)
#front = (0, 0, -1)
left = (-1, 0, 0)
#back = (0, 0, 1)
source.set_rolloff_factor(0)
r = 3
pi = np.pi
#positions = np.linspace(-5, 5, 11)

positions = [left, right, left, right]
random.shuffle(positions)
for degree in positions:
	#position = (r * np.cos(degree), 0, r * np.sin(degree))
	#position = (0, 0, degree)
	source.set_position(degree)
	source.play()
	while source.get_state() == AL_PLAYING:
		# wait until the file is done playing
		time.sleep(1)
		source.stop()

print(positions)

oalQuit()