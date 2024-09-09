import pygame
from typing import Tuple, Optional, List, Dict
from abc import ABC, abstractmethod
from src.game_objects.game_object import GameObject
from src.scenes.scene import Scene

class Game(ABC):
  def __init__(self, scene: Scene, game_objects: List[GameObject]) -> None:
    self._scene = scene
    self._game_objects: List[GameObject] = game_objects
    self._stop: bool = False

    self._collider_groups: Dict[str, List[GameObject]] = {}

    self._x: Optional[float] = None
    self._y: Optional[float] = None

    for game_object in self._game_objects:
      for layer in game_object.get_layers():
        if layer in self._collider_groups:
          self._collider_groups[layer].append(game_object)
        else:
          self._collider_groups[layer] = [game_object]

  def _should_stop(self) -> None:
    return self._stop

  @abstractmethod
  def _handle_event(self, event: pygame.event.Event) -> None:
    pass

  def run(self):
    pygame.init()
    self._scene.start_scene()
    screen = self._scene.get_screen()

    for game_object in self._game_objects:
      game_object.start()

    while not self._should_stop():
      for event in pygame.event.get():
        self._handle_event(event)

      screen.fill('white')

      for game_object in self._game_objects:
        game_object.update()

      for layer, colliders in self._collider_groups.items():
        for i in range(len(colliders)):
          for j in range(i + 1, len(colliders)):
            if colliders[i].is_colliding(colliders[j]):
              colliders[i].on_collide(colliders[j], layer)
              colliders[j].on_collide(colliders[i], layer)

      for game_object in self._game_objects:
        game_object.update_scene()

      pygame.display.flip()

    pygame.quit()
