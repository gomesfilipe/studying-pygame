import pygame
from typing import Tuple, Optional, List
from abc import ABC, abstractmethod
from src.game_objects.game_object import GameObject
from src.scenes.scene import Scene

class Game(ABC):
  def __init__(self, scene: Scene) -> None:
    pygame.init()
    self._scene = scene
    self._game_objects: List[GameObject] = []
    self._stop: bool = False

  def _should_stop(self) -> None:
    return self._stop

  @abstractmethod
  def _build(self) -> None:
    pass


  @abstractmethod
  def _handle_event(self, event: pygame.event.Event) -> None:
    pass

  def run(self):
    self._scene.start_scene()
    self._build()
    screen = self._scene.get_screen()

    for game_object in self._game_objects:
      game_object.start()

    while not self._should_stop():
      for event in pygame.event.get():
        self._handle_event(event)

      screen.fill('white')

      for game_object in self._game_objects:
        game_object.update()
        game_object.update_scene()

      self._scene.render_scene()

    pygame.quit()
