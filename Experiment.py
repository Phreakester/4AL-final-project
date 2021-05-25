from Sound import Sound
import random
import time
import openal
import os
import json

class Experiment:
    def __init__(self, size):  # add onto constructor later
        self.experiment_size = size
        self.sound_list = []
        self.results = []

    def run_experiment(self):
        for sound_obj in self.sound_list:
            time.sleep(random.random() * 2 + 1)
            sound_obj.test()

    def fill_results(self):
        if self.results:
            print("There are already results stored for this experiment, overwrite? (y/n): ")
            if input() != 'y':
                return

        for sound_obj in self.sound_list:
            self.results.append(sound_obj.response_time)

class ControlExperiment(Experiment):
    def construct_experiment(self):
        for i in range(self.experiment_size):
            self.sound_list.append(Sound(0))

class DirectionExperiment(Experiment):
    def construct_experiment(self):
        left = 90
        right = -90
        for i in range(self.experiment_size):
            trial = Sound(random.choice([left, right]))
            self.sound_list.append(trial)

#This is for left right with some angle offset
class AngledExperiment(Experiment):
    def construct_experiment(self):
        left = 90
        right = -90
        for i in range(self.experiment_size):
            direction = random.choice([left, right])
            offset = random.random() * 45
            sign = random.choice([-1,1])
            trial = Sound(direction + sign * offset)
            self.sound_list.append(trial)

class TypeOfSound(Experiment):
    def __init__(self, size):
        Experiment.__init__(self, size)
        self.sound_dictionary = {}
        self.sounds = os.listdir('./sounds')
        for sound in self.sounds:
            self.sound_dictionary[sound] = []

    def construct_experiment(self):
        for i in range(self.experiment_size):
            sound = random.choice(self.sounds)
            trial = Sound(0, './sounds/' + sound)
            self.sound_list.append(trial)

    def fill_results(self):
        for sound_obj in self.sound_list:
            self.sound_dictionary[sound_obj.sound_path[9:]].append(sound_obj.response_time)
        self.results = self.sound_dictionary
            

if __name__ == "__main__":
    input("This is a control. Press m when you hear a sound. Press enter to begin the experiment.")
    control = ControlExperiment(50)
    control.construct_experiment()
    control.run_experiment()
    control.fill_results()

    input("A sound will play from your left or right. Press z if its from your left and m if its from your right. Press enter to begin next experiment.")

    direction = DirectionExperiment(100)
    direction.construct_experiment()
    direction.run_experiment()
    direction.fill_results()

    input("Press m when you hear a sound. Press enter to begin next experiment.")

    randomSounds = TypeOfSound(100)
    randomSounds.construct_experiment()
    randomSounds.run_experiment()
    randomSounds.fill_results()

    input("Play music, press enter when you hear the control sound. Press enter to begin final experiment")
    music = ControlExperiment(50)
    music.construct_experiment()
    music.run_experiment()
    music.fill_results()
    openal.oalQuit()

    data = {}
    data['Control'] = control.results
    data['Direction'] = direction.results
    data['Type of Sound'] = randomSounds.results
    data['Music'] = music.results

    with open('results.json', 'w') as file:
        json.dump(data, file)

