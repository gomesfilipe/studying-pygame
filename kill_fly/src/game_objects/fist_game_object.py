from typing import Dict, Optional, Callable, List
from src.game_objects.game_object import GameObject
import math
from typing import Tuple
from src.utils.utils import lerp
from src.scenes.scene import Scene
import time
import pygame

class FistGameObject(GameObject):
  def __init__(
      self,
      sprites: Dict[str, Tuple[str, Tuple[int, int]]],
      scene: Scene,
      delta_time: int,
      velocity: float,
      layers: List[str] = [],
    ) -> None:
    super().__init__(sprites, scene, layers)

    self._delta_time = delta_time
    self._velocity = velocity

    self._key_handlers = self.__key_handlers()

    self._theta: Optional[float] = None
    self._vx: Optional[float] = None
    self._vy: Optional[float] = None

  @GameObject._start_decorator
  def start(self) -> None:
    self._current_image = self._images['fist']
    self._x = 0.0
    self._y = self._scene.get_display().height()
    self._theta = 0.0

  def update(self) -> None:
    self.__handle_pressed_keys()

  def update_scene(self) -> None:
    screen = self._scene.get_screen()
    screen.blit(self._current_image, (self._x, self._y))

  def __vertical_move(self, angle: int) -> None:
    screen = self._scene.get_screen()
    display = self._scene.get_display()
    self._theta = math.radians(angle)
    self._vy = self._velocity * math.sin(self._theta)
    self._y = lerp(self._y + self._vy * self._delta_time, display.height(), screen.get_height() - self._current_image.get_height())

  def __horizontal_move(self, angle: int) -> None:
    screen = self._scene.get_screen()
    self._theta = math.radians(angle)
    self._vx = self._velocity * math.cos(self._theta)
    self._x = lerp(self._x + self._vx * self._delta_time, 0, screen.get_width() - self._current_image.get_width())

  def __move_up(self) -> None:
    self.__vertical_move(-90)

  def __move_down(self) -> None:
    self.__vertical_move(90)

  def __move_left(self) -> None:
    self.__horizontal_move(-180)

  def __move_right(self) -> None:
    self.__horizontal_move(0)

  def __key_handlers(self) -> Dict[str, Callable]:
    return {
      pygame.K_UP: self.__move_up,
      pygame.K_DOWN: self.__move_down,
      pygame.K_LEFT: self.__move_left,
      pygame.K_RIGHT: self.__move_right,
    }

  def __handle_pressed_keys(self) -> None:
    pressed_keys = pygame.key.get_pressed()

    for key, handler in self._key_handlers.items():
      if pressed_keys[key]:
        handler()

  def on_collide(self, other: GameObject, layer: str) -> None:
    handlers: Dict[str, Callable] = {
      'collision': self.__handle_collision_layer,
    }

    handlers[layer]()

  def __handle_collision_layer(self) -> None:
    return
