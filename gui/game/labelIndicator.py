import simpleGE

class IndicatorLabel(simpleGE.Label):
    FLOAT_DISTANCE = -20
    FRAMES_TO_FLOAT = 20

    def __init__(self):
        super().__init__()

        self.text = "+_"
        self.fgColor = "black"
        self.clearBack = True
        self.center = (-200, -200)

        self.inUse = False
        self.framesFloated = 0
    
    def process(self):
        if self.inUse:
            self.float()
            self.resetIfNeeded()


    def resetIfNeeded(self):
        if self.needsReset():
            self.reset()

    def needsReset(self) -> bool:
        return self.framesFloated >= self.FRAMES_TO_FLOAT

    def reset(self):
        self.inUse = False
        self.framesFloated = 0

        # effectively "hide", but will show again later
        self.center = (-200, -200)
    

    def float(self):
        self.center = self.center[0], self.center[1] + self.FLOAT_DISTANCE / self.FRAMES_TO_FLOAT
        self.framesFloated += 1