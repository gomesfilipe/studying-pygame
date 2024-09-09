from src.games.kill_fly_game import KillFlyGame
from src.scenes.main_scene import MainScene
from src.game_objects.fly_game_object import FlyGameObject

if __name__ == '__main__':
  scene = MainScene((640, 480))

  fly = FlyGameObject(
    {
      'alive': ('sprites/healthy_fly.png', (100, 100)),
      'dead': ('sprites/dead_fly.png', (100, 100)),
    },
    scene,
    delta_time = 1,
    dead_time = 3,
    velocity = 0.1,
  )

  game_objects = [fly]

  game = KillFlyGame(scene, game_objects)
  game.run()
