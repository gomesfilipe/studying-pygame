import pygame
from src.games.game import Game
from src.scenes.scene import Scene
from src.game_objects.fly_game_object import FlyGameObject

class KillFlyGame(Game):
  def __init__(self, scene: Scene) -> None:
    super().__init__(scene)

  def _build(self) -> None:
    self._game_objects = []

    fly = FlyGameObject(
      {
        'alive': ('sprites/healthy_fly.png', (100, 100)),
        'dead': ('sprites/dead_fly.png', (100, 100)),
      },
      self._scene,
      delta_time = 1,
      dead_time = 3,
      velocity = 0.1,
    )

    self._game_objects.append(fly)

  def _handle_event(self, event: pygame.event.Event) -> None:
    handlers = {
      pygame.QUIT: lambda: self.__handle_quit_event()
    }

    handlers.get(event.type, lambda: None)()

  def __handle_quit_event(self) -> None:
    self._stop = True
