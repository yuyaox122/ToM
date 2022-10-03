import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self, screen):
        # general setup
        super().__init__()
        self.screen = screen
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw_sprite(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            # print(sprite.__class__.__bases__)
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.surf, offset_pos)
