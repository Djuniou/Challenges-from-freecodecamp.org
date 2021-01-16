class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def __str__ (self):   
        output = ""
        output += ("Rectangle(width="+str(self.width)+", height="+str(self.height)+")")
        return output
    
    def set_width(self,new_width):
        self.width = new_width
    
    def set_height(self,new_height):
        self.height = new_height
        
    def get_area(self):
        return (self.width*self.height)
    
    def get_perimeter(self):
        return ((2*self.width) + (2*self.height))
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        rect=""
        if ((self.height>50) or (self.width>50)):
            return ("Too big for picture.")
        else:
            for line in range(self.height):
                for column in range (self.width):
                    rect += "*"
                rect += "\n"              
            return rect
    
    def get_amount_inside(self,shape):       
        return int(self.get_area()/shape.get_area())

class Square (Rectangle):
    def __init__(self,side):
        self.side = side   
        self.width = self.side
        self.height = self.side
    def __str__ (self):   
        output = ""
        output += ("Square(side="+str(self.side)+")")
        return output
        
    def set_side(self,new_side):
        self.side = new_side
        self.width = self.side
        self.height = self.side
        
    def set_width(self,new_side):
        self.set_side(new_side)
    
    def set_height(self,new_side):
        self.set_side(new_side)
