import pygame
import math
import random
from typing import Tuple
import time

def lerp(number: float, left: float, right: float) -> float:
  if number < left:
    return left
  elif number > right:
    return right
  else:
    return number

def valid_position(
  i: float,
  j: float,
  image_width: float,
  image_height: float,
  screen_width: float,
  screen_height: float,
) -> bool:
  return i > 0 and i + image_height < screen_height and j > 0 and j + image_width < screen_width

def read_image(path: str, size: Tuple[int, int]):
  image = pygame.image.load(path)
  image = pygame.transform.scale(image, size)
  image = image.convert_alpha()
  return image

def game() -> None:
  pygame.init()
  screen = pygame.display.set_mode((640, 480))
  should_exit = False

  fly_is_dead: bool = False
  dead_time: int = 3

  fist = read_image('sprites/fist.png', (100, 100))
  dead_fly = read_image('sprites/dead_fly.png', (100, 100))
  healthy_fly = read_image('sprites/healthy_fly.png', (100, 100))

  dt: int = 1
  r: float = 0.1

  px: float = random.uniform(0, screen.get_width() - healthy_fly.get_width())
  py: float = random.uniform(0, screen.get_height() - healthy_fly.get_height())
  p_theta: float = math.radians(random.uniform(0, 360))

  fx: float = 0.0
  fy: float = 0.0
  f_theta: float = 0.0

  font = pygame.font.SysFont('impact', 48)

  start_time = time.time()
  score: int = 0

  while not should_exit:
    if not fly_is_dead:
      p_vx = r * math.cos(p_theta)
      p_vy = r * math.sin(p_theta)

      px = lerp(px + p_vx * dt, 0, screen.get_width() - healthy_fly.get_width())
      py = lerp(py + p_vy * dt, 0, screen.get_height() - healthy_fly.get_height())

    fly_image = dead_fly if fly_is_dead else healthy_fly

    fly_rect = fly_image.get_rect(x = px, y = py)
    fist_rect = fist.get_rect(x = fx, y = fy)

    if fist_rect.colliderect(fly_rect) and not fly_is_dead:
      fly_is_dead = True
      fly_respawn_time = time.time() + dead_time
      score += 1

    if fly_is_dead and time.time() >= fly_respawn_time:
      fly_is_dead = False
      px: float = random.uniform(0, screen.get_width() - healthy_fly.get_width())
      py: float = random.uniform(0, screen.get_height() - healthy_fly.get_height())
      p_theta: float = math.radians(random.uniform(0, 360))

    if not valid_position(py, px, healthy_fly.get_width(), healthy_fly.get_height(), screen.get_width(), screen.get_height()):
      p_theta = math.radians(random.uniform(0, 360))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        should_exit = True

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_UP]:
      f_theta = math.radians(-90)
      f_vy = r * math.sin(f_theta)
      fy = lerp(fy + f_vy * dt, 0, screen.get_height() - fist.get_height())

    if pressed_keys[pygame.K_RIGHT]:
      f_theta = math.radians(0)
      f_vx = r * math.cos(f_theta)
      fx = lerp(fx + f_vx * dt, 0, screen.get_width() - fist.get_width())

    if pressed_keys[pygame.K_LEFT]:
      f_theta = math.radians(-180)
      f_vx = r * math.cos(f_theta)
      fx = lerp(fx + f_vx * dt, 0, screen.get_width() - fist.get_width())

    if pressed_keys[pygame.K_DOWN]:
      f_theta = math.radians(90)
      f_vy = r * math.sin(f_theta)
      fy = lerp(fy + f_vy * dt, 0, screen.get_height() - fist.get_height())

    time_spent = int(time.time() - start_time)

    screen.fill("white")

    time_spent_img = font.render(f'Time Spent: {time_spent}', True, (0, 0, 255))
    score_img = font.render(f'Score: {score}', True, (0, 0, 255))

    screen.blit(time_spent_img, (0, 0))
    screen.blit(score_img, (screen.get_width() - score_img.get_width(), 0))
    screen.blit(fist, (fx, fy))
    screen.blit(fly_image, (px, py))
    pygame.display.flip()

  pygame.quit()

if __name__ == '__main__':
  game()
