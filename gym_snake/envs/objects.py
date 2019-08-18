from collections.__init__ import deque

from gym_snake.envs.constants import ObjectColor


class Snake:

    def __init__(
        self,
        x,
        y,
        direction,
        color_head=ObjectColor.own_head,
        color_body=ObjectColor.own_body
    ):
        self.alive = True

        self._color_head = color_head
        self._color_body = color_body

        self._deque = deque()
        self._set = set()
        self._direction = direction

        p = (x, y)
        self._deque.append(p)
        self._set.add(p)

    def __contains__(self, item):
        return item in self._set

    def __iter__(self):
        return self._deque.__iter__()

    def __len__(self):
        return len(self._deque)

    def next_head(self, action):
        head = self._deque[-1]
        direction = self._direction.add_action(action)
        return direction.add_to_point(head)

    def expand(self, action):
        head = self._deque[-1]
        direction = self._direction.add_action(action)
        p = direction.add_to_point(head)

        self._direction = direction
        self._deque.append(p)
        self._set.add(p)

    def contract(self):
        p_last = self._deque.popleft()
        self._set.remove(p_last)

    def kill(self):
        self.alive = False
        self._color_body = ObjectColor.dead_body
        self._color_head = ObjectColor.dead_head

    def render(self, cell_renderer):
        head_id = len(self._deque) - 1
        for i, p in enumerate(self._deque):
            color = self._color_head if (i == head_id) else self._color_body
            cell_renderer(p, color)


class Apples:

    def __init__(self, color=ObjectColor.apple):
        self._set = set()
        self._color = color

    def __contains__(self, item):
        return item in self._set

    def __iter__(self):
        return self._set.__iter__()

    def __len__(self):
        return len(self._set)

    def add(self, p):
        self._set.add(p)

    def remove(self, p):
        self._set.remove(p)

    def render(self, cell_renderer):
        for p in self._set:
            cell_renderer(p, self._color)
