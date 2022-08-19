class weapon():
  def __init__(self,w):
    self.name = w[0]
    self.durability = w[1]
    self.damage = w[2]
    self.range = w[3]
    self.attributes = w[4]
 
class mob():
  def __init__(self, name, theme, type, health, weapon):
    self.name = name
    self.theme = theme
    self.type = type
    self.health = health
    self.weapon = weapon
    
