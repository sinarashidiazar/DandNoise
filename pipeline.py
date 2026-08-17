class Pipeline:

    def __init__(self,filters):

        self.filters = filters

    def process(self,value):

        for f in self.filters:

            if f.enabled:
                value = f.update(value)

        return value
