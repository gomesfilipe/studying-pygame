from src.games.kill_fly_game import KillFlyGame
from src.scenes.main_scene import MainScene
from src.game_objects.fly_game_object import FlyGameObject
from src.game_objects.fist_game_object import FistGameObject
from os.path import join

if __name__ == '__main__':
  SPRITES_PATH: str = 'sprites'
  DELTA_TIME: int = 1
  VELOCITY: float = 0.1

  scene = MainScene((640, 480))

  fly = FlyGameObject(
    {
      'alive': (join(SPRITES_PATH, 'healthy_fly.png'), (100, 100)),
      'dead': (join(SPRITES_PATH, 'dead_fly.png'), (100, 100)),
    },
    scene,
    delta_time = DELTA_TIME,
    dead_time = 3,
    velocity = VELOCITY,
    layers = ['collision']
  )

  fist = FistGameObject(
    {
      'fist': (join(SPRITES_PATH, 'fist.png'), (100, 100)),
    },
    scene,
    delta_time = DELTA_TIME,
    velocity = VELOCITY,
    layers = ['collision']
  )

  game_objects = [fly, fist]

  game = KillFlyGame(scene, game_objects)
  game.run()
