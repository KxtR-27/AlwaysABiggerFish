import pygame, simpleGE, inputActions as Inputs


class PlayerSprite(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        
        self.speed = 5
        self.gameSize = 40

        self.setImage("assets/player.png")
        self.setSize(self.gameSize, self.gameSize)
    
    def process(self):
        # drifting to a stop
        self.dx *= 0.9
        self.dy *= 0.9

        if Inputs.isActionPressed(self, Inputs.Actions.MOVE_LEFT):
            self.dx = -self.speed
        if Inputs.isActionPressed(self, Inputs.Actions.MOVE_RIGHT):
            self.dx = self.speed
        if Inputs.isActionPressed(self, Inputs.Actions.MOVE_UP):
            self.dy = -self.speed
        if Inputs.isActionPressed(self, Inputs.Actions.MOVE_DOWN):
            self.dy = self.speed


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