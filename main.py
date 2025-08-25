import simpleGE
from utils import InputActions
from utils import BoundaryLogic as Bounds

class PlayerSprite(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        
        self.speed = 3
        self.gameSize = 33
        self.driftReductionFactor = 0.9

        self.setImage("assets/player.png")
        self.setSize(self.gameSize, self.gameSize)
        self.setBoundAction(self.CONTINUE)
        
    
    def process(self):
        # drifting to a stop
        self.dx *= self.driftReductionFactor
        self.dy *= self.driftReductionFactor

        if InputActions.isActionPressed(self, InputActions.MOVE_LEFT):
            self.dx = -self.speed
        if InputActions.isActionPressed(self, InputActions.MOVE_RIGHT):
            self.dx = self.speed
        if InputActions.isActionPressed(self, InputActions.MOVE_UP):
            self.dy = -self.speed
        if InputActions.isActionPressed(self, InputActions.MOVE_DOWN):
            self.dy = self.speed
        
        # custom boundary action
        Bounds.ifAtBoundThenForceAway(self)


class GameScene(simpleGE.Scene):
    def __init__(self, size=...):
        super().__init__(size)

        self.setCaption("Eat smaller fish to get bigger!")
        self.setImage("assets/backdrop.png")

        self.player = PlayerSprite(self)

        self.sprites = [
            self.player
        ]


def main():
    resolution = (960, 540)

    game = GameScene(resolution)
    game.start()

if __name__ == "__main__":
    main()