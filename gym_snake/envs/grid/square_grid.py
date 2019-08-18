from gym_snake.envs.constants import Action4, Direction4
from gym_snake.envs.grid.base_grid import BaseGrid


class SquareGrid(BaseGrid):

    def __init__(self, *args, **kwargs):
        super(SquareGrid, self).__init__(*args, **kwargs)

    def get_forward_action(self):
        return Action4.forward

    def get_random_direction(self):
        return Direction4(self.np_random.randint(0, len(Direction4)))

    def get_renderer_dimensions(self, tile_size):
        return self.width * tile_size, self.height * tile_size

    def render(self, r, tile_size, cell_pixels):
        r_width, r_height = self.get_renderer_dimensions(tile_size)
        assert r.width == r_width
        assert r.height == r_height

        # Total grid size at native scale
        width_px = self.width * cell_pixels
        height_px = self.height * cell_pixels

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
        for rowIdx in range(0, self.height):
            y = cell_pixels * rowIdx
            r.drawLine(0, y, width_px, y)
        for colIdx in range(0, self.width):
            x = cell_pixels * colIdx
            r.drawLine(x, 0, x, height_px)

        # Render the objects
        snake_cell_renderer = SquareGrid._square_cell_renderer(r, cell_pixels)
        for snake in self.snakes:
            snake.render(snake_cell_renderer)

        apple_cell_renderer = SquareGrid._circle_cell_renderer(r, cell_pixels)
        self.apples.render(apple_cell_renderer)

        r.pop()

    @staticmethod
    def _square_cell_renderer(r, cell_pixels):
        points = (
            (0,           cell_pixels),
            (cell_pixels, cell_pixels),
            (cell_pixels, 0),
            (0,           0)
        )

        def cell_renderer(p, color):
            x, y = p

            r.push()
            r.setLineColor(*color)
            r.setColor(*color)
            r.translate(x * cell_pixels, y * cell_pixels)
            r.drawPolygon(points)
            r.pop()

        return cell_renderer

    @staticmethod
    def _circle_cell_renderer(r, cell_pixels):
        center_coordinate = cell_pixels / 2
        circle_r = cell_pixels * 10 / 32

        def cell_renderer(p, color):
            x, y = p

            r.push()
            r.setLineColor(*color)
            r.setColor(*color)
            r.translate(x * cell_pixels, y * cell_pixels)
            r.drawCircle(center_coordinate, center_coordinate, circle_r)
            r.pop()

        return cell_renderer
