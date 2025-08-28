from fish import Fish
from presets import FishPresets
from utils import *


class Player(Fish):
    def __init__(self, scene) -> None:
        super().__init__(scene)

        self.applyPreset(FishPresets.PLAYER.value)
        self.DRAG_FACTOR = 0.9

        self.MAX_IFRAMES = 5
        self.remainingIFrames = 0

    def process(self) -> None:
        # drifting to a stop
        self.dx *= self.DRAG_FACTOR
        self.dy *= self.DRAG_FACTOR

        if InputActions.isActionPressed(self, InputActions.MOVE_LEFT):
            self.dx = -self.swimSpeed
            ImageManip.flipFish(self)
        if InputActions.isActionPressed(self, InputActions.MOVE_RIGHT):
            self.dx = self.swimSpeed
            ImageManip.unflipFish(self)
        if InputActions.isActionPressed(self, InputActions.MOVE_UP):
            self.dy = -self.swimSpeed
        if InputActions.isActionPressed(self, InputActions.MOVE_DOWN):
            self.dy = self.swimSpeed

        # custom boundary action
        BoundaryLogic.ifAtBoundThenForceAway(self)

        if self.remainingIFrames > 0:
            self.remainingIFrames -= 1
            # print(f"remaining iframes: {self.remainingIFrames}/{self.MAX_IFRAMES}")


    def growBy(self, addend: int) -> None:
        self.setImage("assets/player.png")
        self.flipped = False

        self.power += addend
        ImageManip.normalizeSizeToPower(self)


    def isInvincible(self) -> bool:
        return self.remainingIFrames > 0

    def triggerIFrames(self) -> None:
        self.remainingIFrames = self.MAX_IFRAMES
