import pygame, simpleGE
from enum import Enum


class InputActions(Enum):
    # Action     WASD         arrow keys      keypad; overlap on purpose for diagonals
    MOVE_LEFT =  [pygame.K_a, pygame.K_LEFT,  pygame.K_KP7, pygame.K_KP4, pygame.K_KP1]
    MOVE_RIGHT = [pygame.K_d, pygame.K_RIGHT, pygame.K_KP9, pygame.K_KP6, pygame.K_KP3]
    MOVE_DOWN =  [pygame.K_s, pygame.K_DOWN,  pygame.K_KP1, pygame.K_KP2, pygame.K_KP3]
    MOVE_UP =    [pygame.K_w, pygame.K_UP,    pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]

    def isActionPressed(sprite: simpleGE.Sprite, action) -> int:
        keysPressed = 0

        for keybind in action.value:
            if sprite.isKeyPressed(keybind):
                keysPressed += 1

        return keysPressed


class BoundaryLogic:
    class _Boundaries(Enum):
        # values are angles at which to force a sprite
        LEFT = 0
        RIGHT = 180
        UP = 270
        DOWN = 90
        NOT_AT_BOUND = -1

    def ifAtBoundThenForceAway(sprite: simpleGE.Sprite) -> None:
        boundary = BoundaryLogic._whereIs(sprite)

        if boundary == BoundaryLogic._Boundaries.NOT_AT_BOUND:
            return
        else:
            BoundaryLogic._forceAwayFrom(sprite, boundary)

    def _whereIs(sprite: simpleGE.Sprite) -> _Boundaries:

        if sprite.x >= sprite.screenWidth:
            return BoundaryLogic._Boundaries.RIGHT
        elif sprite.x <= 0:
            return BoundaryLogic._Boundaries.LEFT
        elif sprite.y >= sprite.screenHeight:
            return BoundaryLogic._Boundaries.DOWN
        elif sprite.y <= 0:
            return BoundaryLogic._Boundaries.UP
        else:
            return BoundaryLogic._Boundaries.NOT_AT_BOUND

    def _forceAwayFrom(sprite: simpleGE.Sprite, bound) -> None:
        sprite.addForce(5, bound.value)


class ImageManip:
    def normalizeSizeToPower(fish: simpleGE.Sprite) -> None:
        aspectRatio = ImageManip._imageAspectRatio(fish)

        normalizedX = fish.power * aspectRatio[0]
        normalizedY = fish.power * aspectRatio[1]

        fish.setSize(normalizedX, normalizedY)

    def _imageAspectRatio(fish: simpleGE.Sprite) -> tuple:
        imageRect = fish.image.get_rect()
        nearCorner = imageRect.topleft
        farCorner = imageRect.bottomright

        dimensions = ImageManip._subtractTuples(farCorner, nearCorner)
        x = dimensions[0]
        y = dimensions[1]

        if x > y:
            return (1, y / x)
        elif y > x:
            return (x / y, 1)
        else:
            return (1, 1)

    def _subtractTuples(tuple1: tuple, tuple2: tuple) -> tuple:
        return (tuple1[0] - tuple2[0], tuple1[1] - tuple2[1])

    def flipIfNeeded(fish: simpleGE.Sprite) -> None:
        if fish.movingRight:
            ImageManip._unflipFish(fish)
        else:
            ImageManip._flipFish(fish)

    def _flipFish(fish: simpleGE.Sprite) -> None:
        if not fish.flipped:
            ImageManip._flipImage(fish)

    def _unflipFish(fish: simpleGE.Sprite) -> None:
        if fish.flipped:
            ImageManip._flipImage(fish)

    def _flipImage(sprite: simpleGE.Sprite) -> None:
        sprite.image = pygame.transform.flip(sprite.image, True, False)
        sprite.flipped = not sprite.flipped


class FontBuilder:
    def withSize(size: int) -> pygame.font.Font:
        return pygame.font.SysFont("", size)