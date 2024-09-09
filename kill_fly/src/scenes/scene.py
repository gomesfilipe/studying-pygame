import pygame
from abc import ABC, abstractmethod
from typing import Tuple, Optional

class Scene(ABC):
  def __init__(self, screen_size: Tuple[int, int]) -> None:
    self._screen_size = screen_size
    self._screen: Optional[pygame.Surface] = None

  @abstractmethod
  def start_scene(self) -> None:
    pass

  def get_screen(self) -> Optional[pygame.Surface]:
    return self._screen