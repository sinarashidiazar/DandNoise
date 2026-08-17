from filters.base import FilterBase

class LowPassFilter(FilterBase):

    name = "Low Pass"

    def __init__(self, alpha=0.1):
        super().__init__()
        self.alpha = alpha
        self.last = None

    def update(self, value):

        if self.last is None:
            self.last = value
        else:
            self.last = self.alpha * value + (1-self.alpha)*self.last

        return self.last
