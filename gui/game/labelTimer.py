import simpleGE

class TimerLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()

        self.text = "Time Left: ???"
        self.center = (560, 50)

        self.fgColor = "black"
        self.clearBack = True