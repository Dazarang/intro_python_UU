# Traffic system components


class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        self.destination = destination
        self.borntime = borntime
    
    def __str__(self):
        return f'Vehicle({self.destination}, {self.borntime})'

class Lane:
    "Represents a lane with (possible) vehicles"

    def __init__(self, length):
        self.lane = [None] * length

    def __str__(self):
        return '[' + ''.join(['.' if x is None else x.destination for x in self.lane]) + ']'
    
    def enter(self, vehicle):
        if self.is_last_free():
            self.lane[-1] = vehicle
        return None  

    def is_last_free(self):
        return self.lane[-1] == None

    def step(self):
        for i in range(len(self.lane) - 1 ):
            if self.lane[i] == None:
                self.lane[i] = self.lane[i+1]
                self.lane[i+1] = None

    def get_first(self):
        return self.lane[0]

    def remove_first(self):
        if self.get_first() != None:
            firstV = self.lane[0]
            self.lane[0] = None
            return firstV
              
    def number_in_lane(self):
        return len(self.lane) - self.lane.count(None)
    


def demo_lane():
    """For demonstration of the class Lane"""
    a_lane = Lane(10)
    print(a_lane)
    v = Vehicle('N', 34)
    a_lane.enter(v)
    print(a_lane)

    a_lane.step()
    print(a_lane)
    for i in range(20):
        if i % 2 == 0:
            u = Vehicle('S', i)
            a_lane.enter(u)
        a_lane.step()
        print(a_lane)
        if i % 3 == 0:
            print('  out: ',
                  a_lane.remove_first())
    print('Number in lane:',
          a_lane.number_in_lane())


class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        self.period = period
        self.green_period = green_period
        self.internalClock = 0

    def __str__(self):
        if self.internalClock <= self.green_period-1:
            return "(G)"
        return "(R)"

    def __repr__(self):
        pass

    def step(self):
        if self.internalClock < self.period-1:
            self.internalClock += 1
        else: 
            self.internalClock = 0

    def is_green(self):
        return self.internalClock <= self.green_period - 1


def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3)
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step()


def main():
    """Demonstrates the classes"""
    print('\nLight demonstration\n')
    demo_light()
    print('\nLane demonstration')
    demo_lane()


if __name__ == '__main__':
    main()
