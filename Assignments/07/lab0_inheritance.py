"""
One final issue with classes we want to deal with is called inheritance. Inheritance is the ability create a class based
on some other class, inheriting all of it's properties, and then adding more. This is very useful in programming when
we are designing reusable parts. You make simple parts, and then you can make more complex parts out of the simple parts
while still keeping the simple part in case you want to modify it later.
"""

""" Here, we define an animal class that has some basic properties, and one action it can take"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.can_move = True
        self.can_grow = True

    def say_hello(self):
        print("\nMy name is {}".format(self.name))


""" Now we are going to create a new class that inherits the Animal class but adds its own properties"""


class Bird(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.has_wings = True
        self.has_feathers = True
        self.can_fly = True

    def say_tweet(self):
        print("Tweet, tweet, tweet!")


""" You should notice a couple of things. First, we pass the class we are inheriting from as an input argument into the 
class definition. Look at Animal's class definition. It doesnt have an input argument. This is fine. That means it's a
base class. Compare that to Bird, it has Animal as an input argument.

Next, look inside Bird's init function. You can see that the first line inside this function is calling Animal's init
function. This is the step that gives all of Animal's attributes and methods to the new Bird class.

Now let's look at what happens when we create them"
"""

animal_list = [Animal("Jon"), Bird("Tweety")]

for animal in animal_list:
    animal.say_hello()
    try:
        animal.say_tweet()
    except:
        pass

    for item in animal.__dict__:
        print("\t", item, animal.__dict__[item])

""" As you can see from this code, Tweety the bird inherits all the attributes and functions of animal."""
# create two more classes:
#   00) snake: which should inherit from Animal
#   01) eagle: which should inherit from Bird
#   Give each new class some unique attributes and a unique method. Then repeat the code from line 41-53, showing off
#      their attributes and methods.

