import LowerBlock
class Player :
    def __init__(self, name) :
        self.name = name
        self.lowerBlock = LowerBlock.LowerBlock()
        self.upperBlock = UpperBlock.UpperBlock()
    def getLowerBlock(self) :
        return self.lowerBlock
    def getUpperBlock(self) :
        return self.upperBlock
