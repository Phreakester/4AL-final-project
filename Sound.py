import time
import random
import keyboard
import openal
import numpy as np

class Sound():
  def __init__(self, position = 90, sound_path = None):
    self.position = position
    if sound_path:
      self.sound_path = sound_path
    else:
      self.sound_path = './sounds/cymbalnew.wav'

    self.source = openal.oalOpen(self.sound_path)

    self.response_time = None

  def playSound(self):
    #Play audio from library, using self.position
    #NOTE: Only plays sound, does not collect data
    xpos = -5*np.sin(self.position*np.pi/180)
    zpos = -5*np.cos(self.position*np.pi/180)
    #print("Playing sound... at: ", self.position , " degrees from straight ahead")
    self.source.set_position((xpos,0,zpos ))
    self.source.play() #Play sound

  def test(self):
    initial_time = time.time()
    self.playSound()
    if self.position >= 90:
        keyboard.wait('z')
    else:
        keyboard.wait('m')
    final_time = time.time()
    self.response_time = final_time - initial_time

if __name__ == "__main__":
    print("Running two sounds, one in front of you (z) and one to the right")
    test1 = Sound()
    test1.test()
    test2 = Sound(-90)
    test2.test()
    print(test1.response_time)
    print(test2.response_time)

