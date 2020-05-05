
class Snake():
class Apple():

class Game(): 
  def __init__(self, height, width):
    self.height = height
    self.width = width
  

  def render(self):
    print ("Height: ", + self.height)
    print ("Width:  ", + self.width)
  

parameters_of_board = Game(10,20)

parameters_of_board.render()
