import time
import random
import keyboard

class Sound():
  def __init__(self, position = 90, sound = None):
    self.position = position
    if sound:
      self.sound = sound
    else:
      self.sound = 'DEFAULT FILE PATH'

    self.response_time = None
  def playSound(self):
    #Play audio from library, using self.position
    #NOTE: Only plays sound, does not collect data
    print("Playing sound...")
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
    test2 = Sound(40)
    test2.test()
    print(test1.response_time)
    print(test2.response_time)

