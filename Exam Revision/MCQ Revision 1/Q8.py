class Fraction: 
  def __init__(self, top=0, bottom=1): 
    self.num = top 
    self.den = bottom 
  def __repr__(self): 
    return 'Fraction({0}, {1})'.format(self.num, self.den) 
  def __str__(self): 
    return str(self.num) + '/' + str(self.den)
x = Fraction(1) 
print(repr(x))