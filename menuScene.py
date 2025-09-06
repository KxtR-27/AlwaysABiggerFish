import pygame, simpleGE
from utils import FontBuilder as NewFont
from gameScene import GameScene

class TitleLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.font = NewFont.withSize(50)

        self.text = "Always A Bigger Fish"
        self.size = (400, 45)
        self.center = (320, 75)
        self.fgColor = "white"
        self.bgColor = "navy"

class SubtitleLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.font = NewFont.withSize(25)

        self.text = 'by Kat R. for CS 439 "First Game"'
        self.font.set_italic(True)
        self.size = (400, 30)
        self.center = (320, 110)
        self.fgColor = "gray"
        self.bgColor = "navy"


class BestSizeLabel(simpleGE.Label):
    def __init__(self, bestSize: int):
        super().__init__()
        self.font = NewFont.withSize(50)
        self.text = f"Best Size: {bestSize}"
        self.center = (320, 220)
        self.size = (400, 50)
        self.clearBack = True
        self.fgColor = "white"

class BestCauseLabel(BestSizeLabel):
    def __init__(self, bestCause: str):
        super().__init__(None)
        self.font: pygame.font.Font = NewFont.withSize(25)
        self.text = f"Cause of Death: {bestCause}"
        self.font.set_italic(True)
        self.center = (self.center[0], self.center[1] + 40)
        self.fgColor = "lightgray"


class PlayButton(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.font = NewFont.withSize(40)

        self.text = "Play"
        self.size = (195, 40)
        self.center = (215, 400)

class QuitButton(PlayButton):
    def __init__(self):
        super().__init__()

        self.text = "Quit"
        self.center = (420, 400)


class MenuScene(simpleGE.Scene):
    def __init__(self, bestSize: int, bestCause: str):
        super().__init__()

        self.setImage("assets/background_menu.png")

        self.titleLabel = TitleLabel()
        self.subtitleLabel = SubtitleLabel()

        self.bestSizeLabel = BestSizeLabel(bestSize)
        self.bestCauseLabel = BestCauseLabel(bestCause)

        self.playButton = PlayButton()
        self.quitButton = QuitButton()

        self.nextAction = ""
        self.buttonSound = simpleGE.Sound("assets/button.wav")

        self.sprites = [
            self.subtitleLabel, self.titleLabel,
            self.bestSizeLabel, self.bestCauseLabel,

            self.playButton, self.quitButton
        ]
    
    def process(self):
        if self.playButton.clicked:
            self.buttonSound.play()
            self.nextAction = "Play"
            self.stop()
        if self.quitButton.clicked:
            self.buttonSound.play()
            self.nextAction = "Quit"
            self.stop()