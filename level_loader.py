
class level():
    def __init__(self, tiles, camera):
        self.level_tiles = tiles
        self.level_camera = camera
        self.level_gravity = 3
    def render(self, window_size):
        for tile in self.level_tiles:
            if tile:
                tile.render_offset[0] = self.level_camera.x
                tile.render_offset[1] = self.level_camera.y
                tile.level_gravity = self.level_gravity
                tile.group = self.level_tiles
                if not tile.x > window_size[0]+30 or tile.x < -30 or tile.y > window_size[1]+30 or tile.y < -30:
                    tile.update()