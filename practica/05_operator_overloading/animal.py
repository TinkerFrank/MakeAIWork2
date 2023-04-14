import unittest

class myAnimal():
    # Docstring to document the purpose, will show up on-hover
    """
    This is an animal class
    """

    def __init__(self, sound, color='black'):
        # attributes
        # Encapsulated in object
        self.snd = sound
        self.color = color

    def setSound(self, input):
        self.assertTrue('FOO'.isupper())
        self.snd = input

    def get_type(self) -> str:  # showes return type on-hover
        if (self.snd == 'woof'):
            return f'My {self.color} animal is a labrador'
        elif (self.snd == 'bark'):
            return "My animal is a Poodle"
        elif (self.snd == 'miauw'):
            return "My animal is a cat"
        else:
            return "My animal is unkown"


class myDog(myAnimal):
    # cant put variables behind a default value (so always put predefined at the end)
    def __init__(self, sound, walktime, color='black'):
        super().__init__(sound, color)
        self.wtime = walktime

    def setWalktime(self, q) -> int:
        self.wtime = q  # why wont a subclass method not update????

    def getWalktime(self) -> str:
        return f'my dog needs {self.wtime} hours of walktime per day'


class mynumber():
    def __init__(self, a):
        self.a = a

    def __add__(self, b):
        return(self.a*b)


#unittest
if __name__ == '__main__':
    snuffy = myAnimal('woof')
    print(snuffy.get_type())
