import constants


class RendererComponent():
    def __init__(self, sprite):
        self.sprite = sprite

    def draw(self, surface, x, y):
        surface.blit(self.sprite, (x * constants.CELL_WIDTH,
                                   y * constants.CELL_HEIGHT))


class HealthComponent():
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.hp = max_hp


class RangedWeaponComponent():
    def __init__(self, name, ammoCapacity, damage, range, area, reloadTurns):
        self.name = name
        self.ammoCapacity = ammoCapacity
        self.damage = damage
        self.range = range
        self.area = area
        self.currentAmmo = ammoCapacity
        self.reloadTurns = reloadTurns
        self.reloading = 0


class Equipment():
    def __init__(self, main_weapon, secondary_weapon):
        self.main_weapon = main_weapon
        self.secondary_weapon = secondary_weapon


class IsPlayer():
    pass


class IsDead():
    pass
