import simpleGE, enum, random

from utils import InputActions
from utils import BoundaryLogic as Bounds


class Fish(simpleGE.Sprite):
    class _States(enum.Enum):
        BEFORE_SCREEN = enum.auto()
        ON_SCREEN = enum.auto()
        AFTER_SCREEN = enum.auto()

    def __init__(self, scene: simpleGE.Scene, gameSize: int, speed, image: str):
        super().__init__(scene)

        self.gameSize = gameSize

        self.setImage(image)
        self.setSize(gameSize, gameSize)
        self.setBoundAction(self.CONTINUE)
        self.dx = speed
        
        self.state = Fish._States.BEFORE_SCREEN
    
    def process(self):
        if self._onScreen() and self.state is Fish._States.BEFORE_SCREEN:
            self.state = Fish._States.ON_SCREEN

        if not self._onScreen() and self.state is Fish._States.ON_SCREEN:
            self.state = Fish._States.AFTER_SCREEN
    
    def _onScreen(self):
        return (0 <= self.x <= self.screenWidth) and (0 <= self.y <= self.screenHeight)


class BasicFish(Fish):
    def __init__(self: Fish, scene: simpleGE.Scene, gameSize: int, speed, image: str):
        super().__init__(scene, gameSize, speed, image)
        self.dx = speed


class PlayerFish(simpleGE.Sprite):
    def __init__(self, scene: simpleGE.Scene):
        super().__init__(scene)
        
        self.speed = 3
        self.gameSize = 33
        self.driftReductionFactor = 0.9

        self.setImage("assets/player.png")
        self.setSize(self.gameSize, self.gameSize)
        self.setBoundAction(self.CONTINUE)
    
    def updateGameSize(self, addend: int):
        self.gameSize += addend
        self.setSize(self.gameSize, self.gameSize)

    
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

        self.player = PlayerFish(self)
        self.fishes = []

        for _ in range (5):
            self.spawnButterflyFish()
        self.spawnShark()
        

        self.sprites = [
            self.player,
            self.fishes
        ]
    
    def process(self):
        for fish in self.fishes:
            if fish.state is Fish._States.AFTER_SCREEN:
                self.fishes.remove(fish)
                print("Fish removed!")
            
            if fish.collidesWith(self.player):
                if fish.gameSize >= self.player.gameSize:
                    print(f"You died! Your size was: {self.player.gameSize}")
                    self.stop()
                else:
                    fish.x = -1000
                    self.player.updateGameSize(fish.gameSize * 0.25)
    
    def spawnButterflyFish(self):
        self._spawnBasicFish(30, random.randint(2, 6), "assets/basicfish_butterfly.png")
    
    def spawnShark(self):
        self._spawnBasicFish(100, random.randint(8, 15), "assets/basicfish_shark.png")

    def _spawnBasicFish(self, gameSize, speed, image):
        fishToSpawn = BasicFish(self, gameSize, speed, image)
        spawnOnLeftSide = random.randint(0, 1)

        if spawnOnLeftSide:
            fishToSpawn.x = random.randint(20, 100) * -1
        else:
            fishToSpawn.x = random.randint(20, 100) + self.screen.get_width()
            fishToSpawn.dx *= -1
        
        fishToSpawn.y = random.randint(0, self.screen.get_height())
        self.fishes.append(fishToSpawn)


def main():
    resolution = (960, 540)

    game = GameScene(resolution)
    game.start()

if __name__ == "__main__":
    main()