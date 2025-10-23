class person:

    def __init__(self, newName):
        self.name = newName
        
person1 = person("ivan")
print(person1.name)
print(person1)

############################################

class animal:

    def __init__(self, Manimals):
        self.animals = Manimals

x = "bearsss"
animalchosen = animal(x)
print(animalchosen.animals)

########################

("""class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()""")

########################################

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)