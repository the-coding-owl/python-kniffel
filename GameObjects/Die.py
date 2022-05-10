import random
import Errors.DieFixedError

class Die :
    def __init__(self) :
        self.face = 1
        self.fixed = false
    def roll(self) :
        if not self.fixed :
            self.face = random.randint(1,6)
        else :
            raise Errors.DieFixedError("This Die is fixed and can not be rolled")
    def getFace(self) :
        return self.face
    def fix(self) :
        self.fixed = true
    def unfix(self) :
        self.fixed = false
    def isFixed(self) :
        return self.fixed
