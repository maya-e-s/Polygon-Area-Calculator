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
        if self.width>50 or self.height>50:
            return "Too big for picture."
        else: 
            ret = ''
            for i in range(self.height):
                ret += '*'*self.width + '\n'
            return ret

    # Returns the number of times the passed in shape could fit inside the shape (with no rotations)
    def get_amount_inside(self, rect_inst):
        return (self.width//rect_inst.width) * (self.height//rect_inst.height)

#class Square(Rectangle):


# test --------------------------------------------
a = Rectangle(10, 5)
b = Rectangle(2, 2)
c = Rectangle(7, 3)

print(a)
print(a.get_picture())
print(b.get_picture())
print(c.get_picture())

print(a.get_amount_inside(b), a.get_amount_inside(c), a.get_amount_inside(a))
print(c.get_amount_inside(a), c.get_amount_inside(b))

