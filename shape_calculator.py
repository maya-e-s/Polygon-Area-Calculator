class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)
    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    # Returns a string that represents the shape using lines of "*"
    def get_picture(self):
        if self.width>50 or self.height>50: return "Too big for picture."
        else: return ('*'*self.width + '\n')*self.height

    # Returns the number of times the passed in shape could fit inside the shape (with no rotations)
    def get_amount_inside(self, rect_inst):
        return (self.width//rect_inst.width) * (self.height//rect_inst.height)

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    # if an instance of a Square is represented as a string, it should look like: Square(side=9)
    def __str__(self):
        return 'Square(side=' + str(self.side) + ')'

    def set_side(self, new_side):
        self.side = new_side
        super().set_width(new_side)
        super().set_height(new_side)

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_height(self, new_height):
        self.set_side(new_height)