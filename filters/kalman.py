from filters.base import FilterBase

class KalmanFilter(FilterBase):

    name = "Kalman"

    def __init__(self):

        super().__init__()

        self.x = 0.0
        self.P = 1.0

        self.Q = 0.01
        self.R = 0.2

    def update(self, z):

        self.P += self.Q

        K = self.P / (self.P + self.R)

        self.x = self.x + K*(z-self.x)

        self.P = (1-K)*self.P

        return self.x
