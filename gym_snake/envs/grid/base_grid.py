import numpy as np

from gym_snake.envs.objects import Apples
from gym_snake.envs.constants import ObjectColor
from gym_snake.envs.objects import Snake


def rotate_color(r, g, b, hue_rotation):
    if hue_rotation == 0:
        return r, g, b

    import colorsys, math
    hue, lightness, saturation = colorsys.rgb_to_hls(r / 255., g / 255., b / 255.)
    r2, g2, b2 = colorsys.hls_to_rgb((hue + hue_rotation) % 1, lightness, saturation)

    return int(math.floor(r2 * 255)), int(math.floor(g2 * 255)), int(math.floor(b2 * 255))


class BaseGrid:

    def __init__(
        self,
        np_random,
        width,
        height,
        num_snakes=1,
        initial_snake_size=4,
        num_apples=1,
        reward_apple=1,
        reward_none=0,
        reward_collision=-1,
        done_apple=False,
        always_expand=False
    ):
        assert width >= initial_snake_size
        assert height >= initial_snake_size
        assert initial_snake_size >= 2

        self.np_random = np_random
        self.num_snakes = num_snakes
        self.width = width
        self.height = height

        self.reward_apple = reward_apple
        self.reward_none = reward_none
        self.reward_collision = reward_collision

        self.done_apple = done_apple
        self.always_expand = always_expand
        self.forward_action = self.get_forward_action()

        self.snakes = None
        self.apples = Apples()
        self.all_done = False

        self.add_snakes(num_snakes, initial_snake_size)
        self.add_apples(num_apples)

    def move(self, actions):
        assert not self.all_done

        rewards = [self.reward_none] * self.num_snakes
        num_new_apples = 0

        # Move live snakes and eat apples
        if not self.always_expand:
            for snake, action in zip(self.snakes, actions):
                if snake.alive:
                    # Only contract if not about to eat apple
                    next_head = snake.next_head(action)
                    if next_head not in self.apples:
                        snake.contract()

        for i, snake, action in zip(range(self.num_snakes), self.snakes, actions):
            if not snake.alive:
                continue

            next_head = snake.next_head(action)
            if self.is_blocked(next_head):
                snake.kill()
                rewards[i] = self.reward_collision
            else:
                snake.expand(action)
                if next_head in self.apples:
                    if self.done_apple:
                        snake.kill()
                    self.apples.remove(next_head)
                    num_new_apples += 1
                    rewards[i] = self.reward_apple

        # If all agents are done, mark grid as done (and prevent future moves)
        dones = [not snake.alive for snake in self.snakes]
        self.all_done = False not in dones

        # Create new apples
        self.add_apples(num_new_apples)

        return rewards, dones

    def encode(self):
        return [self.encode_agent(i) for i in range(self.num_snakes)]

    def __eq__(self, other):
        self_encode = self.encode()
        other_encode = other.encode()

        if len(self_encode) != len(other_encode):
            return False

        for x, y in zip(self_encode, other_encode):
            if not np.array_equal(x, y):
                return False

        return True

    def get_forward_action(self):
        raise NotImplementedError()

    def add_snakes(self, num_snakes=1, initial_snake_size=4):
        self.snakes = []

        for i in range(num_snakes):
            x = self.np_random.randint(0, self.width)
            y = self.np_random.randint(0, self.height)
            direction = self.get_random_direction()

            rotated_green = rotate_color(0, 255, 0, i / num_snakes)
            rotated_blue = rotate_color(0, 0, 255, i / num_snakes)

            new_snake = Snake(x, y, direction, color_head=rotated_blue, color_body=rotated_green)
            self.snakes.append(new_snake)
            for _ in range(initial_snake_size):
                next_head = new_snake.next_head(self.forward_action)
                if self.is_blocked(next_head):
                    # give up and try again to place snakes
                    return self.add_snakes(num_snakes=num_snakes, initial_snake_size=initial_snake_size)

                new_snake.expand(self.forward_action)

    def add_apples(self, num_apples):
        num_open_spaces = self.width * self.height - sum(len(s) for s in self.snakes) - len(self.apples)
        num_new_apples = min(num_apples, num_open_spaces)
        for _ in range(num_new_apples):
            self._add_one_apple()

    def _add_one_apple(self):
        while True:
            p = (self.np_random.randint(0, self.width), self.np_random.randint(0, self.height))
            if self.is_blocked(p) or p in self.apples:
                continue

            self.apples.add(p)
            break

    def is_blocked(self, p):
        x, y = p
        if x < 0 or x >= self.width:
            return True
        if y < 0 or y >= self.height:
            return True

        for snake in self.snakes:
            if p in snake:
                return True

        return False

    def encode_agent(self, agent_number):
        result = np.zeros((self.width, self.height, 3), dtype='uint8')

        for p in self.apples:
            result[p] = ObjectColor.apple

        for i, snake in enumerate(self.snakes):
            if not snake.alive:
                body_color = ObjectColor.dead_body
                head_color = ObjectColor.dead_head
            elif i == agent_number:
                body_color = ObjectColor.own_body
                head_color = ObjectColor.own_head
            else:
                body_color = ObjectColor.other_body
                head_color = ObjectColor.other_head

            last_p = None
            for p in snake:
                result[p] = body_color
                last_p = p

            result[last_p] = head_color

        return result

    def get_random_direction(self):
        raise NotImplementedError()

    def get_renderer_dimensions(self, tile_size):
        raise NotImplementedError()

    def render(self, r, tile_size, cell_pixels):
        raise NotImplementedError()
