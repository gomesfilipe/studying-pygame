import pygame
from src.games.game import Game
from src.scenes.scene import Scene
from src.game_objects.game_object import GameObject
from typing import List

class KillFlyGame(Game):
  def __init__(self, scene: Scene, game_objects: List[GameObject]) -> None:
    super().__init__(scene, game_objects)

  def _handle_event(self, event: pygame.event.Event) -> None:
    handlers = {
      pygame.QUIT: lambda: self.__handle_quit_event()
    }

    handlers.get(event.type, lambda: None)()

  def __handle_quit_event(self) -> None:
    self._stop = True
