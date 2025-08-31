import simpleGE

from gui.game.labelIndicator import IndicatorLabel

class IndicatorManager(simpleGE.Sprite):

    def __init__(self, initialCapacity):
        self.setImage("assets/placeholder.png")
        self.hide()

        self.indicators = []

        for _ in range(initialCapacity):
            self.indicators.append(IndicatorLabel())

    
    def useIndicator(self, value: float, position: tuple[2]):
        indicatorToUse: IndicatorLabel = self._findNextUnusedIndicator()
        indicatorToUse.inUse = True

        indicatorToUse.text = f"+{value}"
        indicatorToUse.center = position

    
    def _findNextUnusedIndicator(self):
        for indicator in self.indicators:
            if not indicator.inUse:
                return indicator
        
        newIndicator = IndicatorLabel()
        self.indicators.append(newIndicator)
        return newIndicator