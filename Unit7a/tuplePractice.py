from collections import namedtuple

person = namedtuple('Person', ['name', 'age'])
persontest = person(name="Alice", age=25)
print(persontest.name)
print(persontest.age)

person1 = person(name="Alice", age=25)
person2 = person(name="Alic", age=24)
person3 = person(name="Ali", age=23)
person4 = person(name="Al", age=22)
person5 = person(name="A", age=21)

people = [person1, person2, person3, person4, person5]
print(people[3].name)
