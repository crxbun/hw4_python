class Base:
    def __init__(self, x, size):
        self.x = x
        self.size = size
    
    def shape(self):
        return "This is a " + str(self.__class__.__name__).lower()

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, size)
        self.y = y

    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """
    
def main():
    c = Circle(1,2,3)
    print(c.shape(), end="")
    print(c.draw())

main()
