from Sound import Sound
import random
import time
import openal
import os

class Experiment:
    def __init__(self, size):  # add onto constructor later
        self.experiment_size = size
        self.sound_list = []
        self.results = []
    #NOTe: Construcor for the actual list provided by children

    def run_experiment(self):
        for sound_obj in self.sound_list:
            time.sleep(random.random() * 2 + 1)
            sound_obj.test()

    def print_results(self):
        if self.results:
            print("There are already results stored for this experiment, overwrite? (y/n): ")
            if input() != 'y':
                return

        for sound_obj in self.sound_list:
            self.results.append(sound_obj.response_time)

        print(self.results)

class CalibrationExperiment(Experiment):
    def construct_experiment(self):
        for i in range(self.experiment_size):
            self.sound_list.append(Sound(0))

class LeftRightExperiment(Experiment):
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

    def print_results(self):
        for sound_obj in self.sound_list:
            self.sound_dictionary[sound_obj.sound_path[9:]].append(sound_obj.response_time)
        print(self.sound_dictionary)

        
        

            

if __name__ == "__main__":
    '''
    print("This is a calibration, only press m");
    calibration = CalibrationExperiment(10)
    calibration.construct_experiment()
    calibration.run_experiment()
    calibration.print_results()

    char = input("Press q to quit")
    if (char == 'q'):
        exit(0)

    example = LeftRightExperiment(5)
    example.construct_experiment()
    example.run_experiment()
    example.print_results()

    input("Press s to continue: ")
    '''
    randomSounds = TypeOfSound(10)
    randomSounds.construct_experiment()
    randomSounds.run_experiment()
    randomSounds.print_results()
    openal.oalQuit()
