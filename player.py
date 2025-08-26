from fish import *
from utils import *

class Player(Fish):
    def __init__(self, scene):
        super().__init__(scene)

        self.applyPreset(FishPresets.PLAYER)
        self.driftReductionFactor = 0.9

    def process(self):
        # drifting to a stop
        self.dx *= self.driftReductionFactor
        self.dy *= self.driftReductionFactor

        if InputActions.isActionPressed(self, InputActions.MOVE_LEFT):
            self.dx = -self.swimSpeed
        if InputActions.isActionPressed(self, InputActions.MOVE_RIGHT):
            self.dx = self.swimSpeed
        if InputActions.isActionPressed(self, InputActions.MOVE_UP):
            self.dy = -self.swimSpeed
        if InputActions.isActionPressed(self, InputActions.MOVE_DOWN):
            self.dy = self.swimSpeed
        
        # custom boundary action
        BoundaryLogic.ifAtBoundThenForceAway(self)
    
    def increasePower(self, addend: int):
        self.setImage("assets/player.png")
        self.power += addend
        self.setSize(self.power, self.power)