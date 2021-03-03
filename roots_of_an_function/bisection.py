class BisectionMethod():
    def __init__(self, x2, x1, x0, interval):
        self.x2 = x2
        self.x1 = x1
        self.x0 = x0
        self.init_interval = interval[0]
        self.end_interval = interval[1]
        self.interval = interval

    def run(self, repeat_limit=100):
        if not(self.__validate()):
            return None

        while repeat_limit > 0:
            root = self.__calculate()
            if root != None:
                return root
            repeat_limit -= 1

        return [self.init_interval, self.end_interval]

    def __calculate(self):
        avg = (self.init_interval + self.end_interval)/2
        value = self.__evaluate(avg)
        if value == 0:
            return avg

        if self.__validate(self.init_interval, avg):
            self.end_interval = avg
        else:
            self.init_interval = avg

        return None

    def __validate(self, init=None, end=None):
        if not(init and end):
            init = self.init_interval
            end = self.end_interval

        if self.__evaluate(init) * self.__evaluate(end) < 0:
            return True
        return False

    def __evaluate(self, point):
        return self.x2 * (point)**2 + self.x1 * point + self.x0
