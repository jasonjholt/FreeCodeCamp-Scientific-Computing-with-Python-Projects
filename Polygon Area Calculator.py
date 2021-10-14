class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, n_width):
    self.width = n_width
  
  def set_height(self, n_height):
    self.height = n_height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    shape = ((self.width * "*") + "\n") * self.height
    return shape

  def get_amount_inside(self, shape):
    return ((self.get_area()) //(shape.get_area()))

class Square(Rectangle):
  def __init__ (self, side):
    self.width = side
    self.height = side
  
  def __str__ (self):
    return f"Square(side={self.width})"
  
  def set_side(self, n_side):
    self.width = n_side
    self.height = n_side
