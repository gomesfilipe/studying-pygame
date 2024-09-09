from typing import Dict, Optional, List, Callable
from src.game_objects.game_object import GameObject
import random
import math
from typing import Tuple
from src.utils.utils import lerp
from src.scenes.scene import Scene
import time

class FlyGameObject(GameObject):
  def __init__(
      self,
      sprites: Dict[str, Tuple[str, Tuple[int, int]]],
      scene: Scene,
      delta_time: int,
      dead_time: int,
      velocity: float,
      layers: List[str] = [],
    ) -> None:
    super().__init__(sprites, scene, layers)

    self._delta_time = delta_time
    self._dead_time = dead_time
    self._velocity = velocity

    self._theta: Optional[float] = None
    self._is_dead: Optional[float] = None
    self._vx: Optional[float] = None
    self._vy: Optional[float] = None
    self._time_to_alive: Optional[float] = None

  @GameObject._start_decorator
  def start(self) -> None:
    self._current_image = self._images['alive']
    self._x, self._y, self._theta = self.__random_position()
    self._is_dead = False

  def update(self) -> None:
    screen = self._scene.get_screen()
    if not self._is_dead:
      if not self._valid_position(self._x, self._y):
        self._theta = self.__random_theta()

      self._vx = self._velocity * math.cos(self._theta)
      self._vy = self._velocity * math.sin(self._theta)

      self._x = lerp(
        self._x + self._vx * self._delta_time,
        0,
        screen.get_width() - self._current_image.get_width()
      )

      self._y = lerp(
        self._y + self._vy * self._delta_time,
        0,
        screen.get_height() - self._current_image.get_height()
      )

    if self._is_dead and time.time() >= self._time_to_alive:
      self._is_dead = False
      self._x, self._y, self._theta = self.__random_position()
      self._current_image = self._images['alive']

  def update_scene(self) -> None:
    screen = self._scene.get_screen()
    screen.blit(self._current_image, (self._x, self._y))

  def on_collide(self, other: GameObject, layer: str) -> None:
    handlers: Dict[str, Callable] = {
      'collision': self.__handle_collision_layer,
    }

    handlers[layer]()

  def __random_theta(self) -> float:
    return math.radians(random.uniform(0, 360))

  def __random_position(self) -> Tuple[float, float, float]:
    screen = self._scene.get_screen()
    x = random.uniform(0, screen.get_width() - self._current_image.get_width())
    y = random.uniform(0, screen.get_height() - self._current_image.get_height())
    theta = self.__random_theta()

    return x, y, theta

  def __handle_collision_layer(self) -> None:
    if not self._is_dead:
      self._is_dead = True
      self._time_to_alive = time.time() + self._dead_time
      self._current_image = self._images['dead']