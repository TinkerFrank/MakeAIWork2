import time as tm
import turtle as tr
import random as rd



# Set up the game window
window = tr.Screen()
window.setup(0.6, 0.6)
window.title("The Python Lunar Landing Game")
window.bgcolor("black")

width = window.window_width()
height = window.window_height()

tr.done()
class Thing:
    def __init__(self,world) -> None:
        self.world = world

    def compute(self):
        pass

    def render(self):
        pass

class Moon(Thing):
    image = 'moon.gif'

    def render(self):
        if self.world.lander.damage>0:
            tr.bgpic('nopic')
            for i in range(int(self.world.lander.damage)):
                tr.bgcolor(rd.choice(('black','white','red','cyan','yellow')))
                tm.sleep(0.01)
            tr.bgpic(self.image)

class Lander(Thing):
    def __init__(self, world) -> None:
        super().__init__(world)

        self.y = 90
        self.v = 0
        self.fuel = 50
    
    def compute(self):
        self.v += self.world.period *(8 if self.firing else -4)
        self.y += self.world.period*self.v

        if self.firing:
            self.fuel -= self.world.period *10
        
        if self.fuel <=0:
            self.fuel = 0
            self.firing = False

        self.damage = 0.1 * self.v**2 if self.y <=0 else 0

        if self.y < 0:
            self.firing = False
            self.y = 0
            self.v = 0



class World:
    def __init__(self) -> None:
        self.moon = Moon(self)
        self.lander = Lander(self)
        self.things = self.moon, self.lander #every thing knows what world it is in and every world knows what things are in it

    def run(self):
        time=tm.time()
        while True:
            oldTime = time
            time = tm.time()
            self.period = time = oldTime

            for thing in self.things:
                thing.compute()

            for thing in self.things:
                thing.render

            tm.sleep(0.05)

World()


