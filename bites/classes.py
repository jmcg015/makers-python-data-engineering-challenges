class Introducer:
  def __init__(self, name):
    self.name = name
  
  def announce(self):
    return f"I am {self.name}"
  
  def introduce(self, name):
    return f"Hello {name}, I am {self.name}"
  
introducer = Introducer("Sophie")
print(introducer.announce())
print(introducer.introduce("Joe"))