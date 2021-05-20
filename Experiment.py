from Sound import Sound

class Experiment:
    def __init__(self, size):  # add onto constructor later
        self.experiment_size = size
        self.sound_list = []
        self.results = []
    #NOTe: Construcor for the actual list provided by children

    def run_experiment(self):
        for sound_obj in self.sound_list:
            sound_obj.test()

    def print_results(self):
        if self.results:
            print("There are already results stored for this experiment, overwrite? (y/n): ")
            if input() != 'y':
                return

        for sound_obj in self.sound_list:
            self.results.append(sound_obj.result)



if __name__ == "__main__":
    example = Experiment(10)
    example.run_experiment()
    example.print_results()

    print("Press s to continue: ")
