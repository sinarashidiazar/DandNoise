import numpy as np

class SensorSimulator:

    def __init__(self):

        self.t = 0
        self.dt = 0.1
        self.noise_std = 0.5

    def update(self):

        self.t += self.dt

        true_value = np.sin(self.t)

        noise = np.random.normal(0,self.noise_std)

        measurement = true_value + noise

        return true_value, measurement
