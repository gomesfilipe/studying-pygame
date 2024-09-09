from src.games.kill_fly_game import KillFlyGame
from src.scenes.main_scene import MainScene

if __name__ == '__main__':
  scene = MainScene((640, 480))
  game = KillFlyGame(scene)

  game.run()
