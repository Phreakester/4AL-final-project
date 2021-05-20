class Experiment:
    def __init__(self, size):  # add onto constructor later
        self.experiment_size = size
        self.sound_list = []

    def run_experiment(self):
        for i in range(self.experiment_size):
            self.sound_list.append(i)  # replace i with sound object

    def print_results(self):
        for i in range(self.experiment_size):
            print(self.sound_list[i])  # print reaction time of sound object


example = Experiment(10)
example.run_experiment()
example.print_results()

print("Press s to continue: ")
