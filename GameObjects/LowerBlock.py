class LowerBlock :
    def __init__(self) :
        self.threeOfAKindSet = false
        self.threeOfAKind = 0
        self.fourOfAKindSet = false
        self.fourOfAKind = 0
        self.fullHouseSet = false
        self.fullHouse = 0
        self.smallStraightSet = false
        self.smallStraight = 0
        self.largeStraightSet = false
        self.largeStraight = 0
        self.yahtzeeSet = false
        self.yahtzee = 0
        self.chanceSet = false
        self.chance = 0
    def threeOfAKind(self, faces) :
        self.threeOfAKind = faces
        self.threeOfAKindSet = true
    def fourOfAKind(self, faces) :
        self.fourOfAKind = faces
        self.fourOfAKindSet = true
    def fullHouse(self, faces) :
        self.fullHouse = faces
        self.fullHouseSet = true
    def smallStraight(self, faces) :
        self.smallStraight = faces
        self.smallStraightSet = true
    def largeStraight(self, faces) :
        self.largeStraight = faces
        self.largeStraightSet = true
    def yahtzee(self, faces) :
        self.yahtzee = faces
        self.yahtzeeSet = true
    def chance(self, faces) :
        self.chance = faces
        self.chanceSet = true
