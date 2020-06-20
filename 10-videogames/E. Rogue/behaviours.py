import random
import actions 

class Brain():
    def __init__ (self, strategy):
        self.strategy = strategy

    def evaluate(self, actor, map, objects):
        self.strategy.evaluate (actor, map, objects)


class RandomWalkStrategy():
    def evaluate(self, actor, map, objects):
        dx = random.randint(-1, 1)
        dy = 0 if dx != 0 else random.randint(-1, 1)
        actor.next_action = actions.WalkAction(
            actor, 
            map, 
            objects,
            dx, dy
        )