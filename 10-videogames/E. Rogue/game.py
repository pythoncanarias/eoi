import pygame
import constants
import random

from actor import Actor
import actions
import behaviours
import components
import math

from map import Map


#   ____    _    __  __ _____
#  / ___|  / \  |  \/  | ____|
# | |  _  / _ \ | |\/| |  _|
# | |_| |/ ___ \| |  | | |___
#  \____/_/   \_\_|  |_|_____|
#
#


def game_main_loop():
    game_quit = False

    current_actor = 0
    current_action = None

    while not game_quit:

        actor = ACTORS[current_actor]

        is_player = actor.get_component(components.IsPlayer)
        is_alive = actor.get_component(components.IsDead) == None
        if (is_player == None):
            if (is_alive):
                brain = actor.get_component(behaviours.Brain)
                if brain != None:
                    brain.evaluate(actor, CURRENT_MAP, ACTORS)
            else:
                current_actor = (current_actor + 1) % len(ACTORS)

        #
        # INPUT
        #

        events_list = pygame.event.get()
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True

            if is_player and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    actor.next_action = actions.WalkAction(
                        actor, CURRENT_MAP, ACTORS, 0, -1)
                if event.key == pygame.K_DOWN:
                    actor.next_action = actions.WalkAction(
                        actor, CURRENT_MAP, ACTORS, 0, 1)
                if event.key == pygame.K_LEFT:
                    actor.next_action = actions.WalkAction(
                        actor, CURRENT_MAP, ACTORS, -1, 0)
                if event.key == pygame.K_RIGHT:
                    actor.next_action = actions.WalkAction(
                        actor, CURRENT_MAP, ACTORS, 1, 0)

            if is_player and event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                cellX = math.floor(x / constants.CELL_WIDTH)
                cellY = math.floor(y / constants.CELL_HEIGHT)
                print('clicked on ' + str(cellX) + ' ' + str(cellY))
                equipment = actor.get_component(components.Equipment)
                weapon = None
                if event.button == 1:
                    weapon = equipment.main_weapon
                if event.button == 3:
                    weapon = equipment.secondary_weapon
                if weapon != None:
                    actor.next_action = actions.RangeAttackAction(
                        weapon, actor, (cellX, cellY), ACTORS)

        #
        # RESOLVE ACTIONS
        #
        action = actor.get_action()

        if action is not None:
            while (True):
                action_result = action.perform()
                if action_result.alternate == None:
                    break
                action = action_result.alternate

            current_actor = (current_actor + 1) % len(ACTORS)

        draw_game()

    pygame.quit()


def game_initialize():
    global SURFACE_MAIN, GAME, PLAYER, CREATURE, CURRENT_MAP, ACTORS
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((
        constants.MAP_WIDTH * constants.SPRITE_SIZE,
        constants.MAP_HEIGHT * constants.SPRITE_SIZE))

    constants.SPRITES = constants.Sprites()

    PLAYER = Actor(5, 5, "Player",
                   [
                       components.IsPlayer(),
                       components.RendererComponent(constants.SPRITES.PLAYER),
                       components.Equipment(
                           components.RangedWeaponComponent(
                               "Colt", 6, 10, 10, 1, 1),
                           components.RangedWeaponComponent(
                               "Dinamite", 6, 25, 10, 3, 1)
                       )
                   ])

    CREATURE = Actor(16, 16, "Creature",
                     [
                         behaviours.Brain(behaviours.RandomWalkStrategy()),
                         components.RendererComponent(
                             constants.SPRITES.CREATURE),
                         components.HealthComponent(10)
                     ])
    CURRENT_MAP = Map(constants.MAP_WIDTH, constants.MAP_HEIGHT)

    ACTORS = [PLAYER, CREATURE]


#  ____  ____      ___        _____ _   _  ____
# |  _ \|  _ \    / \ \      / /_ _| \ | |/ ___|
# | | | | |_) |  / _ \ \ /\ / / | ||  \| | |  _
# | |_| |  _ <  / ___ \ V  V /  | || |\  | |_| |
# |____/|_| \_\/_/   \_\_/\_/  |___|_| \_|\____|
#


def draw_game():
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    CURRENT_MAP.draw(SURFACE_MAIN)
    for actor in ACTORS:
        renderer = actor.get_component(components.RendererComponent)
        if renderer != None:
            renderer.draw(SURFACE_MAIN, actor.x, actor.y)

    pygame.display.flip()


#
#  Main
#

if __name__ == "__main__":
    game_initialize()
    game_main_loop()
