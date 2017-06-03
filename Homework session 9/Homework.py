import pygame

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

############################# Tính khoảng cách giữa 2 điểm #####################

    def distant(self,a):
        self.b = ((self.x - a.x)**2 +(self.y - a.y)**2)**(1/2)

############################## Tìm trung điểm ##################################

    def halfway(self,a):
        self.half_x = (self.x + a.x)/2
        self.half_y = (self.y + a.y)/2
        print("Trung điểm: ({0},{1})".format(self.half_x , self.half_y))
        return self.half_x, self.half_y

############################## Tìm điểm đối xứng Ox, Oy #########################

    ############### Đối xứng Ox ##################

    def reflect_x(self):
        self.reflect_x = -(self.x)
        print("Đối xứng qua Ox: ({0},0)".format(self.reflect_x))

    ############### Đối xưng Oy ##################

    def reflect_y(self):
        self.reflect_y = -(self.y)
        print("Đối xứng qua Oy: (0,{0})".format(self.reflect_y))

    ############### Đối xứng qua góc tọa độ #######

    def reflect_origin(self):
        self.reflect_x = -(self.x)
        self.reflect_y = -(self.y)
        print("Đối xứng qua góc tọa độ O: ({0},{1})".format(self.reflect_x, self.reflect_y))

print("Câu 1:")
a = Point(4, 2)
b = Point(15, 5)
x = a.distant(a)
a.halfway(b)
a.reflect_x()
a.reflect_y()
a.reflect_origin()



