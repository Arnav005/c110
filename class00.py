
class Car:
  def __init__(self,model,colour,company,speedlimit):

    self.model= model
    self.colour=colour
    self.company=company
    self.speedlimit=speedlimit

  def start(self):
     print("started")
     return " return value is written"

  def stop(self):
     print("stop")
     return " return value is not written"

  def accelerate(self):
     print("accelerate")
     return " something returned"
audi= Car("a6","blue","hyundai",30)
print(audi.start())
print(audi.stop())
print(audi.accelerate())
