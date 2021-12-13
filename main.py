class Color:
    end = '\033[0'
    start = '\033[1;38;2'
    mod = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        red_level = self.red
        green_level = self.green
        blue_level = self.blue
        return f'{self.start};{red_level};{green_level};{blue_level}{self.mod}●{self.end}{self.mod}'

    #def __str__(self):
        #return f'{self.start};{self.red};{self.green};{self.blue}{self.mod}●{self.end}{self.mod}'

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __add__(self, other):
        res = Color((self.red + other.red) // 2, (self.green + other.green) // 2, (self.blue + other.blue) //2)
        return res

    def __hash__(self):
        return hash((self.red, self.green, self.blue))




if __name__ == '__main__':
    red = Color(255, 0, 0)
    print(red)
    c1 = Color(255, 0, 0)
    c2 = Color(255, 0, 0)
    c3 = Color(255, 1, 0)
    print (c1==c2)
    print (c1==c3)
    red1 = Color(255, 0, 0)
    green1 = Color(0, 255, 0)
    print (red1 + green1)
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange2, orange1, red1, green1]
    print(color_list)
    print(set(color_list))

