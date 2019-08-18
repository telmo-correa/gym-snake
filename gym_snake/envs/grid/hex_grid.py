import numpy as np
import math

from gym_snake.envs.constants import Action6, Direction6
from gym_snake.envs.grid.base_grid import BaseGrid

SQRT_3 = np.sqrt(3)


class HexGrid(BaseGrid):

    def __init__(self, *args, **kwargs):
        super(HexGrid, self).__init__(*args, **kwargs)

    def get_forward_action(self):
        return Action6.forward

    def get_random_direction(self):
        return Direction6(self.np_random.randint(0, len(Direction6)))

    def get_renderer_dimensions(self, tile_size):
        # Get around weirdness on ffpmeg rendering
        desired_w = int(math.ceil((self.width + 0.5) * SQRT_3 * tile_size / 2 * (4/3)))
        desired_h = int(math.ceil((self.height * 3 + 1) * tile_size / 4 * (4/3)))

        if desired_w % 2 == 1:
            desired_w += 1

        return desired_w, desired_h

    def render(self, r, tile_size, cell_pixels):
        r_width, r_height = self.get_renderer_dimensions(tile_size)
        assert r.width == r_width
        assert r.height == r_height

        # Total grid size at native scale
        width_px = r_width * cell_pixels / tile_size
        height_px = r_height * cell_pixels / tile_size

        r.push()

        # Internally, we draw at the "large" full-grid resolution, but we
        # use the renderer to scale back to the desired size
        r.scale(tile_size / cell_pixels, tile_size / cell_pixels)

        # Draw the background of the in-world cells black
        r.fillRect(
            0,
            0,
            width_px,
            height_px,
            0, 0, 0
        )

        # Draw grid lines
        r.setLineColor(100, 100, 100)
        r.setLineWidth(cell_pixels / tile_size)
        border_renderer = HexGrid._hex_border_renderer(r, cell_pixels * (4/3), last_row=self.height - 1)
        for x in range(self.width):
            for y in range(self.height):
                border_renderer((x, y))

        # Render the objects
        snake_cell_renderer = HexGrid._hex_cell_renderer(r, cell_pixels * (4/3))
        for snake in self.snakes:
            snake.render(snake_cell_renderer)

        apple_cell_renderer = HexGrid._circle_cell_renderer(r, cell_pixels * (4/3))
        self.apples.render(apple_cell_renderer)

        r.pop()

    @staticmethod
    def _hex_border_renderer(r, cell_pixels, last_row=-1):
        dw = SQRT_3 * cell_pixels / 4
        dh = cell_pixels / 4

        points_all = (
            (dw, 0),
            (2 * dw, dh),
            (2 * dw, 3 * dh),
            (dw, 4 * dh)
        )
        line_nw = (
            (dw, 0),
            (0, dh)
        )
        line_sw = (
            (dw, 4 * dh),
            (0, 3 * dh)
        )
        line_w = (
            (0, dh),
            (0, 3 * dh)
        )

        def cell_renderer(p):
            x, y = p
            dx = 0.5 if y % 2 == 0 else 0

            r.push()
            r.translate((x + dx) * 2 * dw, 3 * y * dh)
            r.drawPolyline(points_all)
            if y == 0 or (y % 2 == 1 and x == 0):
                r.drawPolyline(line_nw)
            if y == last_row or (y % 2 == 1 and x == 0):
                r.drawPolyline(line_sw)
            if x == 0:
                r.drawPolyline(line_w)
            r.pop()

        return cell_renderer

    @staticmethod
    def _hex_cell_renderer(r, cell_pixels):
        dw = SQRT_3 * cell_pixels / 4
        dh = cell_pixels / 4
        points = (
            (dw, 0),
            (2 * dw, dh),
            (2 * dw, 3 * dh),
            (dw, 4 * dh),
            (0, 3 * dh),
            (0, dh),
            (dw, 0)
        )

        def cell_renderer(p, color):
            x, y = p
            dx = 0.5 if y % 2 == 0 else 0

            r.push()
            r.setLineColor(*color)
            r.setColor(*color)
            r.translate((x + dx) * 2 * dw, 3 * y * dh)
            r.drawPolygon(points)
            r.pop()

        return cell_renderer

    @staticmethod
    def _circle_cell_renderer(r, cell_pixels):
        dw = SQRT_3 * cell_pixels / 4
        dh = cell_pixels / 4
        circle_r = cell_pixels * 30 / 128

        def cell_renderer(p, color):
            x, y = p
            dx = 0.5 if y % 2 == 0 else 0

            r.push()
            r.setLineColor(*color)
            r.setColor(*color)
            r.translate((x + dx) * 2 * dw, 3 * y * dh)
            r.drawCircle(dw, 2 * dh, circle_r)
            r.pop()

        return cell_renderer
