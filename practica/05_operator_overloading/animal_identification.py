from animal import *

dog = myAnimal('woof')
print(dog.get_type())

dog.setSound('bark')
print(dog.get_type())

dog.setSound('miauw')
print(dog.get_type())

dog.setSound('tadu tadu tadu')
print(dog.get_type())

fluffy = myDog(dog,2)
print(fluffy.getWalktime())
fluffy.setWalktime(20)
print(fluffy.getWalktime())
fluffy.setSound('woof')
print(fluffy.get_type())

x = mynumber(5)
print(x+10)
