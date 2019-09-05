class UpperBlock :
    def __init__(self) :
        self.combi1Set = false
        self.combi1 = 0
        self.combi2Set = false
        self.combi2 = 0
        self.combi3Set = false
        self.combi3 = 0
        self.combi4Set = false
        self.combi4 = 0
        self.combi5Set = false
        self.combi5 = 0
        self.combi6Set = false
        self.combi6 = 0

    def combi1(self, faces) :
        self.combi1 = faces
        self.combi1Set = true
    def combi2(self, faces) :
        self.combi2 = faces
        self.combi2Set = true
    def combi3(self, faces) :
        self.combi3 = faces
        self.combi3Set = true
    def combi4(self, faces) :
        self.combi4 = faces
        self.combi4Set = true
    def combi5(self, faces) :
        self.combi5 = faces
        self.combi5Set = true
    def combi6(self, faces) :
        self.combi6 = faces
        self.combi6Set = true
