from abc import ABC, abstractmethod
from typing import Dict, Tuple, Optional, Callable, List
from src.scenes.scene import Scene
import pygame

class GameObject(ABC):
  def __init__(
      self,
      sprites: Dict[str, Tuple[str, Tuple[int, int]]],
      scene: Scene,
      layers: List[str] = [],
  ) -> None:
    self._sprites = sprites
    self._scene = scene
    self._layers = layers

    self._x: Optional[float] = None
    self._y: Optional[float] = None

    self._current_image: Optional[pygame.Surface] = None
    self._images: Dict[str, pygame.Surface] = {}

  def _start_decorator(func: Callable) -> Callable:
    def initialize_images(self: 'GameObject') -> None:
      for sprite_name, value in self._sprites.items():
        path, size = value
        self._images[sprite_name] = self._read_image(path, size)

      func(self)

    return initialize_images

  @abstractmethod
  def start(self) -> None:
    pass

  @abstractmethod
  def update(self) -> None:
    pass

  @abstractmethod
  def update_scene(self) -> None:
    pass

  @abstractmethod
  def on_collide(self, other: 'GameObject', layer: str) -> None:
    pass

  def _read_image(self, path: str, size: Tuple[int, int]) -> pygame.Surface:
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, size)
    image = image.convert_alpha()
    return image

  def _valid_position(self, i: float, j: float) -> bool:
    screen = self._scene.get_screen()

    return i > 0 and i + self._current_image.get_width() < screen.get_width() and \
      j > 0 and j + self._current_image.get_height() < screen.get_height()

  def get_layers(self) -> List[str]:
    return self._layers

  def is_colliding(self, other: 'GameObject') -> bool:
    self_rect = self._current_image.get_rect(x = self._x, y = self._y)
    other_rect = other._current_image.get_rect(x = other._x, y = other._y)

    return self_rect.colliderect(other_rect)
