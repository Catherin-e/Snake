
class Snake():
  pass
class Apple():
  pass

class Game(): 
  def __init__(self, height, width):
    self.height = height
    self.width = width
    
  
  def board_matrix(self):
    self.board_matrix  = [[" "] * self.width for x in range(self.height)]
    return self.board_matrix
  
  def render(self):
    print ("Height: ", + self.height)
    print ("Width:  ", + self.width)
    
    matrix = self.board_matrix

    for x in range(self.width):
      matrix[0][x] = "-"
      matrix[self.height - 1][x] = "-"

    for y in range(self.height):
      matrix[y][0] = "|"
      matrix[y][self.width - 1] = "|"

    matrix[0][0] = "+"
    matrix[0][self.width-1] = "+"
    matrix[self.height - 1][0] = "+"
    matrix[self.height - 1][self.width - 1] = "+"

    for row in matrix:
      print(' '.join([str(elem) for elem in row]))
  


parameters_of_board = Game(10,20)
parameters_of_board.board_matrix()
parameters_of_board.render()
