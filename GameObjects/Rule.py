class Rule :
    def __init__(self, name: string, points: int, method: string) :
        self.name = name
        self.points = points
        self.method = method

    def calculatePoints(self, dice) :
        points = self.points
        if (method == 'all') :
            for die in dice :
                points += die.getFace()
        return points
