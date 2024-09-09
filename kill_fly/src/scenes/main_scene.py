from typing import Tuple
from src.scenes.scene import Scene
import pygame

class MainScene(Scene):
  def __init__(self, screen_size: Tuple[int, int]) -> None:
    super().__init__(screen_size)

  def start_scene(self) -> None:
    self._screen = pygame.display.set_mode(self._screen_size)
