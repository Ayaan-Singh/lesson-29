from abc import ABC
class ani (ABC):
    def move(self):
        pass
class human (ani):
    def move(self):
        print ("i can walk and run")
class snake (ani):
    def move(self):
        print ("i can slither")

class dog (ani):
    def move(self):
        print ("i can walk and run ")
class lion (ani):
    def move(self):
        print ("i can walk and run")
r = human()
r.move()
r = snake()
r.move()
r = dog()
r.move()
r = lion()
r.move()