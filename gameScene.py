import simpleGE

from gameSprite import GameSprite

from sprites.player import Player
from sprites.fish import Fish
from sprites.bird import Bird
from sprites.crustacean import Crustacean
from sprites.collectible import Collectible

from gui.game.labelPower import PowerLabel
from gui.game.labelTimer import TimerLabel
from gui.game.indicatorManager import IndicatorManager


class GameScene(simpleGE.Scene):
    PLAYER_GROWTH_FACTOR = 0.05

    NUM_OF_FISHES = 10
    NUM_OF_BIRDS = 2
    NUM_OF_CRUSTACEANS = 3
    NUM_OF_COLLECTIBLES = 3

    TIME_IN_SECONDS = 60
    INDICATOR_CAPACITY = 10

    def __init__(self, size=...) -> None:
        super().__init__(size)

        self.setCaption("Eat smaller fish to get bigger!")
        self.setImage("assets/backdrop.png")

        self.player = Player(self)
        self.player.triggerIFrames()
        self.player.position = (
            self.player.screenWidth / 2,
            self.player.screenHeight / 2,
        )

        self.fishes = []
        self.birds = []
        self.crustaceans = []
        self.collectibles = []
        self.populateAllSprites()

        self.powerLabel = PowerLabel()
        self.timerLabel = TimerLabel()

        self.gameTimer = simpleGE.Timer()
        self.gameTimer.totalTime = self.TIME_IN_SECONDS

        self.sprites = [
            self.player,
            self.player.indicatorManager.indicators,

            self.fishes,
            self.birds,
            self.crustaceans,
            self.collectibles,

            self.powerLabel,
            self.timerLabel
        ]
    
    def populateAllSprites(self) -> None:
        self._populateFishes()
        self._populateBirds()
        self._populateCrustaceans()
        self._populateCollectibles()

    def _populateFishes(self) -> None:
        for _ in range (GameScene.NUM_OF_FISHES):
            self.fishes.append(Fish(self))

    def _populateBirds(self) -> None:
        for _ in range (GameScene.NUM_OF_BIRDS):
            self.birds.append(Bird(self))
    
    def _populateCrustaceans(self) -> None:
        for _ in range (GameScene.NUM_OF_CRUSTACEANS):
            self.crustaceans.append(Crustacean(self))
    
    def _populateCollectibles(self) -> None:
        for _ in range (GameScene.NUM_OF_COLLECTIBLES):
            self.collectibles.append(Collectible(self))


    def process(self) -> None:
        self.runAllCollisionChecks()
        self.updatePowerLabel()
        self.updateTimerLabel()
        self.closeIfTimeUp()


    def runAllCollisionChecks(self):
        for fish in self.fishes:
            self._runPlayerCollisionCheck(fish)
        for bird in self.birds:
            self._runPlayerCollisionCheck(bird)
        for crustacean in self.crustaceans:
            self._runPlayerCollisionCheck(crustacean)
        for collectible in self.collectibles:
            self._runCollectibleCollisionCheck(collectible)

    def _runPlayerCollisionCheck(self, animal: Fish | Bird | Crustacean) -> None:
        if animal.collidesWith(self.player):

            if animal.power > self.player.power and not self.player.isInvincible():
                self.endGame()
            else:
                self._playerEats(animal)

    def _playerEats(self, sprite: GameSprite):
        self.player.triggerIFrames()
        self.player.growBy(sprite.power * GameScene.PLAYER_GROWTH_FACTOR)
        sprite.reset()

    def _runCollectibleCollisionCheck(self, collectible: Collectible):
        if collectible.collidesWith(self.player):
            self.player.triggerIFrames()
            self.player.growBy(collectible.powerGain)
            collectible.reset()
    

    def updatePowerLabel(self) -> None:
        self.powerLabel.text = f"Power: {self.player.power}"

    def updateTimerLabel(self) -> None:
        self.timerLabel.text = f"Time: {self.gameTimer.getTimeLeft():.2f}"
        
    def closeIfTimeUp(self) -> None:
        if self.gameTimer.getTimeLeft() <= 0:
            self.endGame()
        

    def endGame(self) -> None:
        print(f"Power Score: [{self.player.power}]")
        print(f"Time survived: [{self.gameTimer.getElapsedTime():.2f} seconds]")
        exit(0)