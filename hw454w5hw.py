class dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        print("Dog is created")
        
        
    def sit(self):
          print(self.name.title() + "Dog is siting")
          
    def jump(self):
          print(self.name.title() + "JUmping!")
          
    def bark(self):
          print(self.name.title() + "Barking!")
          
my_dog = dog('Topik ', 4)
my_dog_2 = dog('Jack ', 10)
Puppy = dog('Puppy ' , 3)

print(my_dog.age)
print(my_dog.name)

print(my_dog_2.age)
print(my_dog_2.name)

my_dog_2.jump()
my_dog.sit()
Puppy.bark()

