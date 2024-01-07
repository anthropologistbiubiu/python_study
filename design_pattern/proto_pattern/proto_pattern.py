import copy

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def clone(self):
       return copy.deepcopy(self)
    def get_config(self):
        return self.radius

class Rectangle:
    def __init__(self,width,high):
        self.width = width
        self.high = high
    def clone(self):
       return copy.deepcopy(self)
    def get_config(self):
        return self.width,self.high


class GraphEditor:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def print_shape(self):
        for item in self.shapes:
            print(type(item).__name__,item.get_config())


def main():
  circle = Circle(5)
  rectangle = Rectangle(3,4)
  edit = GraphEditor()
  edit.add_shape(circle.clone())
  edit.add_shape(rectangle.clone())
  edit.print_shape()

if __name__ == '__main__':
    main()
