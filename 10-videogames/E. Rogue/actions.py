import components
import behaviours
import math


class ActionResult:
    def __init__(self, success, alternate=None):
        self.alternate = alternate
        self.success = success


class Action:
    def perform(self):
        print("WARNING: Action has no perform")
        return ActionResult(False, None)


class WalkAction(Action):
    def __init__(self, actor, map, objects, dx, dy):
        self.actor = actor
        self.map = map
        self.dx = dx
        self.dy = dy
        self.objects = objects
        self.endingPosition = (0, 0)

    def perform(self):
        xx = self.actor.x + self.dx
        yy = self.actor.y + self.dy

        tile_is_blocked = self.map.tiles[xx][yy].block_path == True
        occupant = None

        for object in self.objects:
            if (object.x == xx and object.y == yy and object is not self.actor):
                occupant = object

        if occupant:
            return ActionResult(False, MeleeAttackAction(self.actor, occupant))

        if tile_is_blocked == False and occupant is None:
            self.actor.x += self.dx
            self.actor.y += self.dy
            self.endingPosition = (
                self.actor.x + self.dx, self.actor.y + self.dy)
            return ActionResult(True)
        else:
            return ActionResult(False, BumpAction(self.actor, self.map, self.objects, xx, yy))


class MeleeAttackAction (Action):
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def perform(self):
        # get melee weapon, use to deal damage
        return ActionResult(False, DamageAction(self.attacker, self.defender, 5))


class RangeAttackAction (Action):
    def __init__(self, rangedWeaponComponent, attacker, attackedCell, objects):
        self.rangedWeaponComponent = rangedWeaponComponent
        self.attacker = attacker
        self.attackedCell = attackedCell
        self.objects = objects

    def perform(self):
        weapon = self.rangedWeaponComponent
        if weapon is None:
            return ActionResult(False, None)

        # get all objects at tilePosition
        for obj in self.objects:
            x, y = self.attackedCell
            print(obj.name)
            print(distance(obj.x, obj.y, x, y))
            print(weapon.range)
            if distance(obj.x, obj.y, x, y) <= weapon.area:
                print(weapon.name + " BANG! hits " + obj.name)
                return ActionResult(False, DamageAction(self.attacker, obj, weapon.damage))

        return ActionResult(True)


class DamageAction (Action):
    def __init__(self, attacker, defender, damage):
        self.attacker = attacker
        self.defender = defender
        self.damage = damage

    def perform(self):
        health = self.defender.get_component(components.HealthComponent)
        if health is None:
            return ActionResult(False, None)

        health.hp = max(0, health.hp - self.damage)
        print("Took damage " + str(5) + ". Life at " + str(health.hp))
        if (health.hp == 0):
            return ActionResult(False, KillAction(self.attacker, self.defender))

        return ActionResult(True)


class KillAction (Action):
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def perform(self):
        print(self.defender.name + " is dead")
        self.defender.remove_component(components.HealthComponent)
        self.defender.add_component(components.IsDead())
        return ActionResult(True)


class BumpAction (Action):
    def __init__(self, actor, map, objects, x, y):
        self.actor = actor
        self.map = map
        self.x = x
        self.y = y
        self.objects = objects

    def perform(self):
        print("BUMP!")
        return ActionResult(True)

#  _   _ _____ _     ____  _____ ____  ____
# | | | | ____| |   |  _ \| ____|  _ \/ ___|
# | |_| |  _| | |   | |_) |  _| | |_) \___ \
# |  _  | |___| |___|  __/| |___|  _ < ___) |
# |_| |_|_____|_____|_|   |_____|_| \_\____/


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
