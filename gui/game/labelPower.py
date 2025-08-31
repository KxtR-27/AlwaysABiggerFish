import simpleGE

class PowerLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()

        self.text = "Power: ???"
        self.center = (300, 50)

        self.fgColor = "black"
        self.clearBack = True