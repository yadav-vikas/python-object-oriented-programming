#Inheritance is a way of creating a new class for using details of an existing class without modifying it. 
# The newly formed class is a derived class (or child class).

#Parent class
class Bird:

    def __init__(self):
        print("bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swim faster")

#child class
class penguin(Bird):

    def __init__(self):
        #calling super() function to access from parent
        super().__init__()
        print("penguin is ready")
    def whoisthis(self):
        print("penguin")
    def run(self):
        print("run faster")

#evaluation
peggy=penguin()
print(peggy.whoisthis())
print(peggy.run())

# we inherited from parent using super()
#child class modified the behavior of parent class from whoisthis() method
#we also extended child class by adding another method run() to
