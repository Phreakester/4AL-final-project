from Sound import Sound
import random
import time
import openal

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
        openal.oalQuit()

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

            

if __name__ == "__main__":
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
