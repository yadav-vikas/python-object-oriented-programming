#Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

class Parrot:

    def fly(self):
        print("parrot flys")
    def swim(self):
        print("parrot shouldnt swims")
    
class penguin:

    def fly(self):
        print("penguin shouldnt fly")

    def swim(self):
        print("penguin can swim")

#common interface using bird as object
def fly(bird):
    bird.fly()

#instance the objects
red = Parrot()
black = penguin()

#evaluation
fly(red)
fly(black)

#common interface using animal as object
def swimmer(animal):
    animal.swim()

#evaluation
swimmer(red)
swimmer(black)

#we had 2 classes parrot and penguin both contain fly and swim method
#as we pass different object -red and black- the results were as expected from swimmer and fly method
