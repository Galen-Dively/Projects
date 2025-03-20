import pytmx
import os
import farmland
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(os.getcwd())
        world_path = f"{os.getcwd()}/src/assets/test.tmx"
        self.world_data = pytmx.load_pygame(world_path)
        self.tiles = []
        self.load_map()

    def load_map(self):
        for layer in self.world_data:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    image = self.world_data.get_tile_image_by_gid(gid)
                    if layer.name == "Farmland":
                        farm = farmland.Farmblock(1, x, y, 16, 16, (10))
                        self.tiles.append({"Tag": "Farmland", "Block": farm})
                    if image:
                        self.tiles.append({"Tag": "Tile", "Image": image, "pos": (x*16, y*16)})


    
    def draw(self, screen, camera_offset_x, camera_offset_y):
        for tile in self.tiles:
            if tile["Tag"] == "Tile":
                adjusted_x = tile["pos"][0] - camera_offset_x
                adjusted_y = tile["pos"][1] - camera_offset_y
                screen.blit(tile["Image"], (adjusted_x, adjusted_y))
            if tile["Tag"] == "Farmland":
                tile["Block"].draw(screen, camera_offset_x, camera_offset_y)
                