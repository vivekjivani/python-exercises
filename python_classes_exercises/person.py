class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def getAge(self):
    return self.age
  
  def getName(self):
    return self.name
  
  def setAge(self, age):
    self.age = age

  def setName(self, name):
    self.name = name
  
  def __str__(self):
    return f'Namae : {self.name} \nAge: {self.age}'.format()


class Student(Person):
  def __init__(self, name, age, rollNumber, standard):
      super().__init__(name, age)
      self.rollNumber = rollNumber
      self.standard = standard
  
  def __str__(self):
    print("{}".format(super().__str__()))
    return f"Std : {self.standard} \nRoll Number : {self.rollNumber}"

# Object Creation

carl = Student("carl", "22", "01", "2")

print(carl)