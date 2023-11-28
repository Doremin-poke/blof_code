class Pokemon:
    def __init__(self,property, name, types, H, A, B, C, D, S, move1, move2, move3, move4, terastal):
        self.name = name
        self.property = property
        self.types = types  # リスト定義する
        self.H = H
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.S = S
        self.moves = [move1, move2, move3, move4]  # 技をリストで保持する
        self.terastal = terastal

class Property:
    def __init__(self, name):
        self.name = name

class EmergeProperty(Property(name)):
    def effect(self):
        if self.name == "Intimidate":
            return "相手の攻撃を下げる"
            
class MoveProperty(Property(name)):
    def effect(self):
        if self.name == "Unseen_Fist":
            return "守る貫通"     

#property
Intimidate = EmergeProperty("Intimidate") 
Unseen_Fist = MoveProperty("Unseen_Fist")


Landorus = Pokemon("Landorus","Intimidate" ,["Fly", "Ground"], 165, 197, 110, 112, 100, 157, Earthquake, U_Turn, Rock_Slide, Protect, "Fly")

