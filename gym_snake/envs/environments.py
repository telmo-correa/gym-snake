from gym_snake.envs.constants import GridType
from gym_snake.envs.snake_env import SnakeEnv


class Snake_4x4_DeadApple(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=4, initial_snake_size=2, done_apple=True)

class Snake_8x8_DeadApple(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=8, done_apple=True)

class Snake_16x16_DeadApple(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=16, done_apple=True)

class Snake_Hex_4x4_DeadApple(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=4, initial_snake_size=2, done_apple=True)

class Snake_Hex_8x8_DeadApple(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=8, done_apple=True)

class Snake_Hex_16x16_DeadApple(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=16, done_apple=True)


class Snake_4x4(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=4, initial_snake_size=2)

class Snake_8x8(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=8)

class Snake_16x16(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=16)

class Snake_Hex_4x4(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=4, initial_snake_size=2)

class Snake_Hex_8x8(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=8)

class Snake_Hex_16x16(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex,grid_size=16)



class Snake_4x4_4a(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=4, initial_snake_size=2, num_apples=4)

class Snake_8x8_4a(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=8, num_apples=4)

class Snake_16x16_4a(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=16, num_apples=4)

class Snake_Hex_4x4_4a(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=4, initial_snake_size=2, num_apples=4)

class Snake_Hex_8x8_4a(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=8, num_apples=4)

class Snake_Hex_16x16_4a(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=16, num_apples=4)



class Snake_4x4_Expand(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=4, initial_snake_size=2, reward_none=1, num_apples=0)

class Snake_8x8_Expand(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=8, always_expand=True, reward_none=1, num_apples=0)

class Snake_16x16_Expand(SnakeEnv):
    def __init__(self):
        super().__init__(grid_size=16, always_expand=True, reward_none=1, num_apples=0)

class Snake_Hex_4x4_Expand(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=4, initial_snake_size=2, reward_none=1, num_apples=0)

class Snake_Hex_8x8_Expand(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=8, always_expand=True, reward_none=1, num_apples=0)

class Snake_Hex_16x16_Expand(SnakeEnv):
    def __init__(self):
        super().__init__(grid_type=GridType.hex, grid_size=16, always_expand=True, reward_none=1, num_apples=0)


class Snake_4x4_DeadApple_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=4, initial_snake_size=2, done_apple=True)

class Snake_8x8_DeadApple_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=8, done_apple=True)

class Snake_16x16_DeadApple_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=16, done_apple=True)

class Snake_Hex_4x4_DeadApple_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=4, initial_snake_size=2, done_apple=True)

class Snake_Hex_8x8_DeadApple_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=8, done_apple=True)

class Snake_Hex_16x16_DeadApple_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=16, done_apple=True)


class Snake_4x4_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=4, initial_snake_size=2)

class Snake_8x8_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=8)

class Snake_16x16_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=16)

class Snake_Hex_4x4_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=4, initial_snake_size=2)

class Snake_Hex_8x8_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=8)

class Snake_Hex_16x16_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex,grid_size=16)



class Snake_4x4_4a_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=4, initial_snake_size=2, num_apples=4)

class Snake_8x8_4a_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=8, num_apples=4)

class Snake_16x16_4a_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=16, num_apples=4)

class Snake_Hex_4x4_4a_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=4, initial_snake_size=2, num_apples=4)

class Snake_Hex_8x8_4a_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=8, num_apples=4)

class Snake_Hex_16x16_4a_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=16, num_apples=4)



class Snake_4x4_Expand_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=4, initial_snake_size=2, reward_none=1, num_apples=0)

class Snake_8x8_Expand_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=8, always_expand=True, reward_none=1, num_apples=0)

class Snake_16x16_Expand_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_size=16, always_expand=True, reward_none=1, num_apples=0)

class Snake_Hex_4x4_Expand_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=4, initial_snake_size=2, reward_none=1, num_apples=0)

class Snake_Hex_8x8_Expand_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=8, always_expand=True, reward_none=1, num_apples=0)

class Snake_Hex_16x16_Expand_2s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=2, grid_type=GridType.hex, grid_size=16, always_expand=True, reward_none=1, num_apples=0)


class Snake_4x4_DeadApple_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=4, initial_snake_size=2, done_apple=True)

class Snake_8x8_DeadApple_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=8, done_apple=True)

class Snake_16x16_DeadApple_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=16, done_apple=True)

class Snake_Hex_4x4_DeadApple_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=4, initial_snake_size=2, done_apple=True)

class Snake_Hex_8x8_DeadApple_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=8, done_apple=True)

class Snake_Hex_16x16_DeadApple_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=16, done_apple=True)


class Snake_4x4_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=4, initial_snake_size=2)

class Snake_8x8_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=8)

class Snake_16x16_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=16)

class Snake_Hex_4x4_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=4, initial_snake_size=2)

class Snake_Hex_8x8_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=8)

class Snake_Hex_16x16_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex,grid_size=16)



class Snake_4x4_4a_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=4, initial_snake_size=2, num_apples=4)

class Snake_8x8_4a_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=8, num_apples=4)

class Snake_16x16_4a_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=16, num_apples=4)

class Snake_Hex_4x4_4a_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=4, initial_snake_size=2, num_apples=4)

class Snake_Hex_8x8_4a_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=8, num_apples=4)

class Snake_Hex_16x16_4a_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=16, num_apples=4)



class Snake_4x4_Expand_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=4, initial_snake_size=2, reward_none=1, num_apples=0)

class Snake_8x8_Expand_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=8, always_expand=True, reward_none=1, num_apples=0)

class Snake_16x16_Expand_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_size=16, always_expand=True, reward_none=1, num_apples=0)

class Snake_Hex_4x4_Expand_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=4, initial_snake_size=2, reward_none=1, num_apples=0)

class Snake_Hex_8x8_Expand_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=8, always_expand=True, reward_none=1, num_apples=0)

class Snake_Hex_16x16_Expand_3s(SnakeEnv):
    def __init__(self):
        super().__init__(num_snakes=3, grid_type=GridType.hex, grid_size=16, always_expand=True, reward_none=1, num_apples=0)
